import sys
import os
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_app.settings')
django.setup()

from django.urls import path
from . import views

urlpatterns = [
    path('eos', views.index, name='index'),

]