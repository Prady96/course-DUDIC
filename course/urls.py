from django.contrib import admin
from django.urls import path, include
from .views import *
from login import views

urlpatterns = [
    path('', course_page, name='index'),
    path('lectures/<str:course_name>', lecture_page, name='lecture_page'),
    path('login/', views.login_page),
    # path('PDF/', GeneratePDF.as_view()),
    path('testPDF/', generate_pdf, name='generate_pdf'),
]
