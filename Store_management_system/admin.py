from django.contrib import admin
from .models import *
# from .models import Company,Medicine
# from .models import Medical_Details
# from .models import Employee
# from .models import Customer
# from .models import Bill
# from .models import Employee_Salary
# from .models import Bill_Details
# from .models import Customer_Request
# from .models import Company_Account
# from .models import Company_Bank
# from .models import Employee_Bank

class CompanyAdminModel(admin.ModelAdmin):
      list_display = ['id','name', 'licence_no','address','contact_no','email','added_on']
    # if you want to edit the filed then following list_editable option can be added 
    #  list_editable = ['name','contact_no','address']

class MedicineAdminModel(admin.ModelAdmin):
    list_display = ['id','name','medical_type','buy_price','sell_price','batch_no','shelf_no','exp_date','mfg_date','company_id','stock_remaining','qty_in_strip','added_on']

class EmployeeAdminModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'employee', 'joining_date' , 'phone' , 'address' , 'added_on']

class CustomerAdminModel(admin.ModelAdmin):
    list_display = ['id','name','address','contact','added_on']

class BillAdminModel(admin.ModelAdmin):
    list_display = ['id','customer_id','added_on']    

class EmployeeSalaryAdminModel(admin.ModelAdmin):
    list_display = ['id','employee_id','salary_date','salary_amount','added_on']


class BillDetailsAdminModel(admin.ModelAdmin):
    list_display = ['id','bill_id','medical_id','qty','added_on']


# Register your models here.
admin.site.register(Company, CompanyAdminModel)
admin.site.register(Medicine, MedicineAdminModel)
admin.site.register(Employee, EmployeeAdminModel)
admin.site.register(Customer, CustomerAdminModel)
admin.site.register(Bill, BillAdminModel)
admin.site.register(Employee_Salary, EmployeeSalaryAdminModel)
