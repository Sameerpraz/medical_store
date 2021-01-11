from django.urls import path
from . import views
from .views import HomeView, AddPostView, UpdateView


urlpatterns = [
    path("", views.index, name="dashboard"),
    path("company",HomeView.as_view(),name='index'),
    path("company/add/",AddPostView.as_view(),name='create'),
    # path("",UpdateView.as_view(),name='update'),
    
]