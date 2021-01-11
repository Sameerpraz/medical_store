from django.db import models
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('index')

class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    medical_type = models.CharField(max_length=50)
    buy_price = models.CharField(max_length=50)
    sell_price = models.CharField(max_length=50)
    batch_no = models.CharField(max_length=50)
    shelf_no = models.CharField(max_length=50)
    exp_date = models.DateField()
    mfg_date = models.DateField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    stock_remaining = models.IntegerField()
    qty_in_strip = models.IntegerField()
    added_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    def get_success_url(self):
        return reverse('index')




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
    
    def get_success_url(self):
        return reverse('index')


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    added_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    def get_success_url(self):
        return reverse('index')

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    added_on = models.DateField(auto_now_add=True)


    def get_success_url(self):
        return reverse('index')



class Employee_Salary(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_date = models.DateField(auto_now_add=True)
    salary_amount = models.IntegerField()
    added_on = models.DateField(auto_now_add=True)

    def get_success_url(self):
        return reverse('index')


