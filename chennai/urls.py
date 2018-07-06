from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('leave/', views.leave, name='leave'),
    path('completed/', views.completed, name='completed'),
    path('search/', views.search, name='search'),
    path('email_autocomplete/', views.email_autocomplete, name='email_autocomplete')
]
