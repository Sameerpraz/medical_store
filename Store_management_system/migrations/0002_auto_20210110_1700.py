# Generated by Django 3.1 on 2021-01-10 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store_management_system', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_bank',
            old_name='ifcs_no',
            new_name='ifsc_no',
        ),
    ]
