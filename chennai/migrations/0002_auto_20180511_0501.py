# Generated by Django 2.0.5 on 2018-05-10 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chennai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveformmodel',
            name='lead_approved_time_stamp',
            field=models.DateTimeField(null=True),
        ),
    ]
