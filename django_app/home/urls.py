from django.urls import path
from . import views

urlpatterns = [
    path('eos', views.index, name='index'),

]