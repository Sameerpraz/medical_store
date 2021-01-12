from django.urls import path
from . import views
from .views import HomeView, AddCategoryView, CategoryUpdateView ,DeleteCategory


urlpatterns = [
    path("", views.index, name="dashboard"),
    path('company',HomeView.as_view(),name='index'),
    path('company/add/',AddCategoryView.as_view(),name='create'),
    path('company/edit/<int:pk>/' , CategoryUpdateView.as_view() , name='update'),
    path('company/<int:pk>/delete' , DeleteCategory.as_view() , name='delete'),
    
]