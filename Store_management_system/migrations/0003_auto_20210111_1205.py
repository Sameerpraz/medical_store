# Generated by Django 3.1.5 on 2021-01-11 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store_management_system', '0002_auto_20210110_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill_details',
            name='bill_id',
        ),
        migrations.RemoveField(
            model_name='bill_details',
            name='medical_id',
        ),
        migrations.RemoveField(
            model_name='company_account',
            name='company_id',
        ),
        migrations.RemoveField(
            model_name='company_bank',
            name='company_id',
        ),
        migrations.DeleteModel(
            name='Customer_Request',
        ),
        migrations.RemoveField(
            model_name='employee_bank',
            name='employee_id',
        ),
        migrations.RemoveField(
            model_name='medical_details',
            name='medicine_id',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='c_gst',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='description',
        ),
        migrations.DeleteModel(
            name='Bill_Details',
        ),
        migrations.DeleteModel(
            name='Company_Account',
        ),
        migrations.DeleteModel(
            name='Company_Bank',
        ),
        migrations.DeleteModel(
            name='Employee_Bank',
        ),
        migrations.DeleteModel(
            name='Medical_Details',
        ),
    ]