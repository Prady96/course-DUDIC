from django.contrib import admin
from django.urls import path, include
from .views import *
from course.views import course_page

urlpatterns = [
    path('', apply_page_new, name='index'),
    path('error/', error_page),
    path('thankyou/', thank_you_page, name='thankyou'),
    path('login/', login_page, name = 'login'),
    path('logout/', logoutUser, name = 'logout'),
    path('course_page/', course_page, name= 'course_page'),
]
