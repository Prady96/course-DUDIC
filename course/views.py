from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
# from login.urls import *
from login.models import *


@login_required(login_url='login/')
def course_page(request):
    # import pdb;pdb.set_trace()
    logged_in_user_email = request.user.email
    applicant = ApplicationModel.objects.filter(email=logged_in_user_email).first()
    course_applied = applicant.course_name
    course_applied_date = applicant.course_date
    course_applied_start_date = applicant.course_date.start_date
    # filtered_course = Course.objects.filter(course_name=course_applied).filter(date=course_applied_date).first()
    filtered_course = Course.objects.filter(course_name=course_applied).filter(date__start_date=course_applied_start_date).first()
    filtered_course_date = filtered_course.date.start_date
    applicant_course_date = applicant.course_date.start_date
    if filtered_course_date == applicant_course_date:
        course_to_be_displayed = Course.objects.filter(course_name=course_applied).filter(date__start_date=course_applied_start_date)
        context = {
        'queryset' : course_to_be_displayed,
        }
        return render(request, 'course_page.html', context)
    else:
        
        """list the course which user has selected"""
        """ Try and Catch for no course found or please apply first before login """
        pass
    return render(request, 'course_page.html')


@login_required(login_url='login/')
def lecture_page(request, course_name):
    # import pdb;pdb.set_trace()
    print(course_name)
    course_name = Course.objects.filter(course_name__name=course_name)[1:].get()
    lectures = lecture.objects.filter(course_name=course_name.id)
    # qs1 = Course.objects.all() 
    # qs = lecture.objects.all()

    # sq = lecture.objects.filter(course_name='3')

    context = {
         'queryset' : course_name,
         'specific' : lectures,
    }
    return render(request, 'main_course_page.html', context)




# @login_required(login_url='login/')
# def lecture_page(request):
#     qs = lecture.objects.all()

#     sq = lecture.objects.filter(course_name='3')

#     context = {
#          'queryset' : qs,
#          'specific' : sq,
#     }
#     return render(request, 'main_course_page.html', context)