import django_tables2 as tables
from .models import LeaveFormModel
from django_tables2.export.views import ExportMixin


class LeaveFormTable(tables.Table):
    export_formats = ['csv']

    class Meta:
        model = LeaveFormModel
        template_name = 'django_tables2/bootstrap4.html'


class TableViews(ExportMixin, tables.SingleTableView):
    table_class = LeaveFormTable
    model = LeaveFormModel
    template_name = 'django_tables2/bootstrap4.html'

