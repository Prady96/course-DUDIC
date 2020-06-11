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
    # from nose.tools import set_trace; set_trace()
    course_applied_start_date = '2020-06-09'
    print(course_name)
    course_name_qs = Course.objects.filter(course_name__name=course_name).filter(date__start_date=course_applied_start_date).get()
    lectures = lecture.objects.filter(course_name=course_name_qs.id)
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

from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
from django.template.loader import get_template

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        template = get_template('certifcate.html')
        context = {
            "invoice_id":123,
        }
        html = template.render(context)
        pdf = render_to_pdf('certifcate.html', context)
        return HttpResponse(pdf, content_type='application/pdf')

######################### weasy print #############################

from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
import tempfile

# if request.POST.get('certi'):
#     print('user requested certi')

@login_required(login_url='login/')
def generate_pdf(request):
    # student_name = 
    # import pdb; pdb.set_trace()
    logged_in_user_email = request.user.email
    applicant = ApplicationModel.objects.filter(email=logged_in_user_email).first()
    certificate_name = certificates_list.objects.filter(name=applicant.name)
    context = {
        'certs' : certificate_name
    }
    html_string = render_to_string('certifcate.html', context)
    # import pdb; pdb.set_trace()
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf(stylesheets=[CSS(settings.STATIC_ROOT +  '/weasy_css.css')], presentational_hints=True)
    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=list_people.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response



















