from django.urls import path
from . import views

urlpatterns = [
    path('', views.process_numbers, name='process_numbers'),
]