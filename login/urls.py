from django.contrib import admin
from django.urls import path, include
from .views import *
from course.views import course_page

from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', apply_page_new, name='index'),
    path('error/', error_page),
    path('thankyou/', thank_you_page, name='thankyou'),
    path('login/', login_page, name = 'login'),
    path('logout/', logoutUser, name = 'logout'),
    path('course_page/', course_page, name= 'course_page'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
