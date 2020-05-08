from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', apply_page_new, name='index'),
    path('error/', error_page),
    path('thankyou/', thank_you_page),
]
