from django.urls import path
from django_app.home import views

urlpatterns=[
    path('',views.index)
]