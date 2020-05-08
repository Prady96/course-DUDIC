from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from dudic.settings import *
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def apply_page(request):
    return render(request, 'fillForm.html')

def apply_page_media(request):
    return render(request, 'fillForm_media.html')

def error_page(request):
    return render(request, '404.html')

def thank_you_page(request):
    return render(request, 'thank_you.html')

def success(request ,name, email, course_name, start_date, end_date, course_id):
    print(name, email, course_name, start_date, end_date )

    if course_id == 'DUDIC01B2':
        course_poster = 'https://dudic.io/wp-content/uploads/2020/05/Innovation-Course6.jpg'
    if course_id == 'DUDIC02B2':
        course_poster = 'https://dudic.io/wp-content/uploads/2020/05/Innovation-Course5.jpg'
    if course_id == 'DUDIC03B2':
        course_poster = 'https://dudic.io/wp-content/uploads/2020/05/Innovation-Course2-1.jpg'
    if course_id == 'DUDIC04B2':
        course_poster = 'https://dudic.io/wp-content/uploads/2020/05/Innovation-Course.jpg'
    if course_id == 'DUDIC05B2':
        course_poster = 'https://dudic.io/wp-content/uploads/2020/05/Innovation-Course3.jpg'
    if course_id == 'CISE01B2':
        course_poster = 'https://dudic.io/wp-content/uploads/2020/05/Innovation-Course-7.jpg'


    template = render_to_string('email_template.html', 
                                {'name'       : name,
                                 'course_name': course_name,
                                 'course_id'  : course_id,
                                 'start_date' : start_date,
                                 'end_date'   : end_date, 
                                 'course_poster' : course_poster})
    email = EmailMessage(
        'Cordinator DIC',
        template,
        settings.EMAIL_HOST_USER,
        [email,]
    )

    email.fail_silently = False
    email.send()
    context = {
            'email' : email, 
    }

    start_date = ''
    end_date = ''




    return render(request, 'thank_you.html', context)


def apply_page_new(request):
    qs = CourseModel.objects.all()
    if request.method == 'POST':

        form = ApplyForm(request.POST or None)    
        
        # import pdb; pdb.set_trace()
        if form.is_valid():
            print(form.cleaned_data)
            name        = form.cleaned_data['name']
            education   = form.cleaned_data['education']
            age         = form.cleaned_data['age']
            address     = form.cleaned_data['address']
            mobile_num  = form.cleaned_data['mobile_num']
            email       = form.cleaned_data['email']
            reason      = form.cleaned_data['reason']
            hear_about  = form.cleaned_data['hear_about']
            course_name = form.cleaned_data['course_name']
            course_date = form.cleaned_data['course_date']
        else:
            print(form.errors)
            context={
                'queryset' : qs,
                'form': form
            }
            return render(request, 'fillForm.html', context)

        ApplicationModel.objects.create(**form.cleaned_data)
        start_date  = course_date.start_date
        end_date    = course_date.end_date
        course_id   = course_name.id
        data = success(request, name, email, course_name, start_date, end_date, course_id)
        print('reached')
        context = {
            'email' : email, 
        }
        return render(request, 'thank_you.html', context)
    form = ApplyForm()
    context = {
        'queryset' : qs,
        'form': form
    }
    return render(request, 'fillForm.html', context)


# def apply_page_new(request):
    



