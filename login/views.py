from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from dudic.settings import *
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

####################### TEST PAGES #######################

def apply_page(request):
    return render(request, 'fillForm.html')

def apply_page_media(request):
    return render(request, 'fillForm_media.html')

def error_page(request):
    return render(request, '404.html')

def thank_you_page(request):
    return render(request, 'thank_you.html')

####################### EMAIL #############################

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


####################### TEMPLATE TAGS #######################

from django import template
register = template.Library()

# @register.filter
# def upper(value1, value2):
#     """Testing Converts a string into all uppercase"""
#     print(value1)
#     print(value2)
#     return value.upper()

# @register.filter
# def people(course_id, course_date):
#     dates = DateModel.objects.filter(course_id = course_id)
#     import pdb;pdb.set_trace()
#     date = dates.filter(start_date=start_date) & dates.filter(end_date=end_date)
#     date
    
#     date = dates.objects.filter(course_date=course_date)
#     date.relateds.all()
#     people_registered = date.relateds.count()
#     return people_registered


# @register.filter
# def number_of_people_registered(course_id, course_date):
#     dates = DateModel.objects.filter(course_id = course_id)
#     import pdb;pdb.set_trace()
#     date = dates.objects.filter(course_date=course_date)
#     date.relateds.all()
#     people_registered = date.relateds.count()
#     return people_registered

####################### CUSTOM FUNCTIONS #######################

def count_number_registerations(course_id):
    """Count number of registeration for each course"""
    qs = DateModel.objects.filter(course_id=course_id)
    for i in range(len(qs)):
        date = DateModel.objects.filter(course_id=course_id)[i]
        print('start_date is', date.start_date)
        values = DateModel.objects.filter(course_id=course_id)[i].relateds.count()
        print('number of registerations done', values)
        ans = DateModel.objects.filter(course_id=course_id).filter(start_date=date.start_date).update(registeration=values)
        print('Values are update Sucessfully', ans)


def update_date_registered_user(course_id, course_date_id):
    """Shifting Candidates Dates"""
    qs = ApplicationModel.objects.filter(course_name_id=course_id)
    number = ApplicationModel.objects.filter(course_name_id=course_id).count()
    print('number of People Registered for this course', number)
    ans = ApplicationModel.objects.filter(course_name_id=course_id).update(course_date_id=course_date_id)
    print('Success', ans)
    count_number_registerations(course_id)
    print('Updated on Main Table')



def update_count_user_registeration(course_id, course_date):
    """After Application Update Registeration"""
    alrdy_regstd = 0
    print('before',alrdy_regstd)
    alrdy_regstd = DateModel.objects.filter(course_id=course_id).get(start_date=course_date.start_date).relateds.count()
    print('after',alrdy_regstd)
    date = DateModel.objects.filter(course_id=course_id).filter(start_date=course_date.start_date)
    date.update(registeration = alrdy_regstd)

####################### MAIN VIEWS ###########################

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
            # import pdb; pdb.set_trace()
        else:
            context={
                'queryset' : qs,
                'form': form,
            }
            return render(request, 'fillForm.html', context)
            print(form.errors)
        ApplicationModel.objects.create(**form.cleaned_data)
        start_date  = course_date.start_date
        end_date    = course_date.end_date
        course_id   = course_name.id
        update_count_user_registeration(course_id, course_date)
        data = success(request, name, email, course_name, start_date, end_date, course_id)
        print('reached')
        context = {
            'email' : email, 
        }
        return render(request, 'thank_you.html', context)
    form = ApplyForm()
    context = {
        'queryset' : qs,
        'form': form,
    }
    return render(request, 'fillForm.html', context)

###############################################################
    



