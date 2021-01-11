from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Employee, Company, Medicine, Customer, Bill, Employee_Salary
from django.urls import reverse_lazy
# Create your views here.


def index(request):
    return render(request, "Dashboard/base.html", {})



class HomeView(ListView):
    model = Company
    template_name = 'Dashboard/Modules/Company/index.html'


class AddPostView(CreateView):
    model = Company
    template_name = 'Dashboard/Modules/Company/create.html'
    fields = '__all__'


    # def add(request):
    #     return render(request,"Dashboard/Modules/Company/create.html")

    



class PostUpdate(UpdateView):
    model = Company
    fields = ['address','contact_no','email']
    template_name = 'Dashboard/Modules/Company/edit.html'

class DeletePost(DeleteView):
    model = Company
    template_name = 'Dashboard/Modules/Company/delete.html'
    success_url = reverse_lazy('index')


