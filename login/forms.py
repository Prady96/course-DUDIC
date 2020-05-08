from django import forms
import re
from .models import *
from django.forms import modelformset_factory
from django.forms import ModelForm , Textarea

class ApplyForm(ModelForm):

    class Meta:
        model = ApplicationModel
        fields = ['name','education','age','address','mobile_num',
                    'email','reason','hear_about','course_name','course_date',
                    'instituteOrStartup','student_details',]
        required = (
            'name',
            'age',
            'address',
            'mobile_num',
            'email',
            'reason',
            'course_name',
            'course_date',
        )

        widgets = {
            'student_details': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

    def clean_email(self):
        # import pdb;pdb.set_trace()
        # print(dir(self))
        email = self.cleaned_data.get('email')
        qs = ApplicationModel.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("This Email has already been used")
        return email

    def clean_mobile_num(self):
        mobile_num = self.cleaned_data.get('mobile_num')
        qs = ApplicationModel.objects.filter(mobile_num=mobile_num)
        if qs.exists():
            raise forms.ValidationError("This mobile_num has already been used")
        return mobile_num

















