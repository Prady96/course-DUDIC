from django import forms
import re
from .models import *
from django.forms import modelformset_factory
from django.forms import ModelForm 

# class ApplyForm(forms.Form):

#     name            = forms.CharField(required = True)
#     education       = forms.CharField()
#     age             = forms.IntegerField(required=True)
#     email           = forms.EmailField(required = True)
#     address         = forms.CharField(required = True)
#     mobile_num      = forms.CharField(required = True)
#     reason          = forms.CharField(widget=forms.Textarea)
#     hear_about_us   = forms.CharField()
#     # courses         = forms.ModelChoiceField(queryset = CourseModel.objects.all().prefetch_related('relateds'))
#     # dates           = forms.ModelChoiceField(queryset= CourseModel.objects.prefetch_related('relateds'))
    

#     def clean_phone_number(self, *args, **kwargs):
#         phone_number = self.cleaned_data.get('phone_number')
#         print(phone_number)
#         if re.match(r'[789]\d{9}$', phone_number):
#             print('yes')
#         else:  
#             print('Phone Number is not valid')
#             raise forms.ValidationError('Phone Number is not valid')
#         return phone_number

class ApplyForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

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

        def clean(self):
            mobile_num = self.cleaned_data.get('mobile_num')
            try:
                if re.match(r'[789]\d{9}$', mobile_num):
                    print('yes')
                else:  
                    print('Phone Number is not valid')
                    raise forms.ValidationError('Phone Number is not valid')
            except:
                pass
            return self.cleaned_data
            # except:
            #     print("exception ")
            

            

    # def clean(self):
    #     super(ApplyForm, self).clean()

    #     mobile_num = self.cleaned_data.get('mobile_num')
    #     print(mobile_num)
    #     try:
    #         if re.match(r'[789]\d{9}$', mobile_num):
    #             print('yes')
    #         else:  
    #             print('Phone Number is not valid')
    #             raise forms.ValidationError('Phone Number is not valid')
    #     except:
    #         print("exception ")
    #     return mobile_num 
















