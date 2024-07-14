from django.contrib import admin
from django.urls import path
from .views import home,contact_view

urlpatterns = [
    path('',home),
    path('contact/', contact_view, name='contact'),
]
