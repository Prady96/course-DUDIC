from django import forms
from .models import *
from django.forms import ModelForm 


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_name','available',
                'instructor','date','course_image',]

class LectureForm(ModelForm):
    class Meta:
        model = lecture
        fields = ['course_name','title','description',
                    'zoom_link','download_resources',
                    'available']

# class CertiForm(M)






















