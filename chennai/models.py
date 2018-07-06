# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ListOfAssociatesChennai(models.Model):
    emp_number = models.CharField(db_column='Emp_Number', primary_key=True, max_length=50, unique=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40)  # Field name made lowercase.
    supervisor = models.CharField(db_column='Supervisor', max_length=40)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True, unique=True)  # Field name made lowercase.
    update_date = models.DateField(db_column='Update_Date')  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=50, blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'List of Associates Chennai'


class LeaveFormModel(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)
    emp_name = models.CharField(max_length=50)
    emp_id = models.IntegerField()
    emp_email = models.EmailField()
    emp_lead = models.CharField(max_length=50)
    leave_start_date = models.DateField()
    leave_end_date = models.DateField()
    lead_approved = models.BooleanField()
    lead_approved_time_stamp = models.DateTimeField(null=True)
    hr_approved = models.BooleanField()
    hr_approved_time_stamp = models.DateTimeField(null=True)
    comments = models.CharField(max_length=250)

    def __str__(self):
        return 'Leave for ' + str(self.emp_name) + ' between ' + str(self.leave_start_date) \
               + ' and ' + str(self.leave_end_date)
