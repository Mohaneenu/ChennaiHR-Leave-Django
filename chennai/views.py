from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django_tables2 import RequestConfig
from django_tables2.export.export import TableExport
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import LeaveForm, SearchForm
from .models import LeaveFormModel, ListOfAssociatesChennai
from .tables import LeaveFormTable

import django_tables2


# Create your views here.


def email_autocomplete(request):
    if request.GET.get('q'):
        q = request.GET['q']
        data = ListOfAssociatesChennai.objects.using('legacy').filter(email__startswith=q).values_list('email',
                                                                                                       flat=True)
        json = list(data)
        return JsonResponse(json, safe=False)
    else:
        HttpResponse("No cookies")


def leave(request):
    if request.method == 'GET':
        form = LeaveForm()
    else:
        form = LeaveForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            comments = form.cleaned_data['comments']
            message = 'leave start from ' + start_date + ' till ' + end_date
            try:
                data = LeaveFormModel(
                    emp_name='',
                    emp_id='1',
                    emp_email=from_email,
                    emp_lead='',
                    leave_start_date=start_date,
                    leave_end_date=end_date,
                    lead_approved=False,
                    hr_approved=False,
                    comments=comments)
                data_emp_check = ListOfAssociatesChennai.objects.using('legacy').get(email=data.emp_email)
                data.emp_name, data.emp_lead = data_emp_check.name, data_emp_check.supervisor
                data.save()
                send_mail(message, message,
                          from_email, ['a3a@anywhere.co'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('completed')
    return render(request, "chennai/leave.html", {'form': form})


def completed(request):
    return render(request, "chennai/completed.html", {})


def search(request):
    table = LeaveFormTable(LeaveFormModel.objects.all())
    if request.method == 'GET':
        form = SearchForm()
    else:
        form = SearchForm(request.Post)
        if form.is_valid():
            try:
                HttpResponse('TEST')
            except BadHeaderError:
                return HttpResponse('invalid header found')
        return redirect('search')
    context = {
        'form': form,
        'table': table
    }
    RequestConfig(request).configure(table)

    export_format = request.GET.get('_export', None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response('table.{}'.format(export_format))

    return render(request, "chennai/search.html", context)
