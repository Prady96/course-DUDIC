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

    def clean_course_date(self):
        # import pdb;pdb.set_trace()
        course_name = self.cleaned_data.get('course_name')
        course_date = self.cleaned_data.get('course_date')
        course_name_1 = course_name
        course_date_1 = course_date
        qs = CourseModel.objects.filter(name=course_name)[0]
        qs.relateds.all()
        q2 = qs.relateds.filter(start_date=course_date_1.start_date)
        q1 = qs.relateds.filter(end_date=course_date_1.end_date)
        if len(q1) == 0 or len(q2) == 0:
            raise forms.ValidationError('Please select one course_date for course_name & disable others')
        if set(list(q1)) != set(list(q2)):
              raise forms.ValidationError('Please select one course_date for course_name & disable others')
        else:
              return course_date
    # 


    # if q1.exists() and str(q1[0]) == course_date_1.end_date:
    #           if q2.exists() and str(q2[0]) == course_date_1.start_date:
    #               return
    #       else:
    #           raise forms.ValidationError("Please Select Date Appropriately")
    #     if not qs.relateds.filter(start_date=start_date) qs.relateds.filter(end_date=end_date):
    #           raise forms.ValidationError('Please select course_date for course_name & disable others')
    #       



















