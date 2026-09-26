from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('forms/',views.forms,name='forms'),

]

