from django.db import models

# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    licence_no = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    added_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"

class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    medical_type = models.CharField(max_length=50)
    buy_price = models.CharField(max_length=50)
    sell_price = models.CharField(max_length=50)
    c_gst = models.CharField(max_length=50)
    batch_no = models.CharField(max_length=50)
    shelf_no = models.CharField(max_length=50)
    exp_date = models.DateField()
    mfg_date = models.DateField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    stock_remaining = models.IntegerField()
    qty_in_strip = models.IntegerField()
    added_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Medical_Details(models.Model):
    id = models.AutoField(primary_key=True)
    medicine_id = models.ForeignKey(Medicine, on_delete = models.CASCADE )
    salt_name = models.CharField(max_length=20)
    salt_qty = models.CharField(max_length=20)
    salt_qty_type = models.CharField(max_length=20)
    added_on = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.salt_name}"


# class Admin(models.Model):
#     id = models.AutoField(primary_key=True)
#     fname = models.CharField(max_len=20)
#     lname = models.CharField(max_len=20)
#     email = models.CharField(max_len=20)
#     password = 
#     last_login =
#     added_on = models.DateField(auto_now_add=True)


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    employee = models.CharField(max_length=20)
    joining_date = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    added_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    added_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    added_on = models.DateField(auto_now_add=True)



class Employee_Salary(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_date = models.DateField(auto_now_add=True)
    salary_amount = models.IntegerField()
    added_on = models.DateField(auto_now_add=True)



class Bill_Details(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    medical_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    qty = models.IntegerField()
    added_on = models.DateField(auto_now_add=True)


class Customer_Request(models.Model):
    id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    medicine_details = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    requested_date = models.DateField()

    def __str__(self):
        return f"{self.cust_name}"

class Company_Account(models.Model):
    choices =((1,"debit"),(2,"credit"))
    id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(Company, on_delete = models.CASCADE)
    trans_type = models.CharField(choices=choices, max_length=20)
    trans_amount = models.CharField(max_length=20)
    trans_date = models.DateField()
    payment_mode = models.CharField(max_length=20)



class Company_Bank(models.Model):
    id = models.AutoField(primary_key=True)
    bank_acc_no = models.CharField(max_length=20)
    ifsc_no = models.CharField(max_length=20)
    company_id = models.ForeignKey(Company,on_delete = models.CASCADE)




class Employee_Bank(models.Model):
    id = models.AutoField(primary_key=True)
    bank_acc_no = models.CharField(max_length=20)
    ifsc_no = models.CharField(max_length=20)
    employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
