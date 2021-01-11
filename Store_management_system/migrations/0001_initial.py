# Generated by Django 3.1.5 on 2021-01-08 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('added_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('licence_no', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('added_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=20)),
                ('added_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cust_name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('medicine_details', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=False)),
                ('requested_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('employee', models.CharField(max_length=20)),
                ('joining_date', models.DateField(auto_now_add=True)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('added_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('medical_type', models.CharField(max_length=50)),
                ('buy_price', models.CharField(max_length=50)),
                ('sell_price', models.CharField(max_length=50)),
                ('c_gst', models.CharField(max_length=50)),
                ('batch_no', models.CharField(max_length=50)),
                ('shelf_no', models.CharField(max_length=50)),
                ('exp_date', models.DateField()),
                ('mfg_date', models.DateField()),
                ('description', models.CharField(max_length=50)),
                ('stock_remaining', models.IntegerField()),
                ('qty_in_strip', models.IntegerField()),
                ('added_on', models.DateField(auto_now_add=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store_management_system.company')),
            ],
        ),
        migrations.CreateModel(
            name='Medical_Details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('salt_name', models.CharField(max_length=20)),
                ('salt_qty', models.CharField(max_length=20)),
                ('salt_qty_type', models.CharField(max_length=20)),
                ('added_on', models.DateField(auto_now_add=True)),
                ('description', models.CharField(max_length=20)),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store_management_system.medicine')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Salary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('salary_date', models.DateField(auto_now_add=True)),
                ('salary_amount', models.IntegerField()),
                ('added_on', models.DateField(auto_now_add=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store_management_system.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Bank',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bank_acc_no', models.CharField(max_length=20)),
                ('ifsc_no', models.CharField(max_length=20)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store_management_system.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Company_Bank',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bank_acc_no', models.CharField(max_length=20)),
                ('ifcs_no', models.CharField(max_length=20)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store_management_system.company')),
            ],
        ),
        migrations.CreateModel(
            name='Company_Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('trans_type', models.CharField(choices=[(1, 'debit'), (2, 'credit')], max_length=20)),
                ('trans_amount', models.CharField(max_length=20)),
                ('trans_date', models.DateField()),
                ('payment_mode', models.CharField(max_length=20)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store_management_system.company')),
            ],
        ),
        migrations.CreateModel(
            name='Bill_Details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('added_on', models.DateField(auto_now_add=True)),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store_management_system.bill')),
                ('medical_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store_management_system.medicine')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store_management_system.customer'),
        ),
    ]
