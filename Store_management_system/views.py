from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Employee, Company, Medicine, Customer, Bill, Employee_Salary
from django.urls import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.


def index(request):
    return render(request, "Dashboard/base.html", {})



class HomeView(ListView):
    model = Company
    template_name = 'Dashboard/Modules/Company/index.html'


class AddCategoryView(CreateView):
    model = Company
    template_name = 'Dashboard/Modules/Company/create.html'
    fields = '__all__'


class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    model = Company
    fields = ['address','contact_no','email']
    success_message = "was created successfully"
    template_name = 'Dashboard/Modules/Company/edit.html'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data
        )

class DeleteCategory(DeleteView):
    model = Company
    template_name = 'Dashboard/Modules/Company/delete.html'
    success_url = reverse_lazy('index')


