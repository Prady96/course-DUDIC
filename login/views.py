from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from dudic.settings import *
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User as system_user

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

def get_poster_link(course_id):
    """ Get poster link """

    if course_id == 'DUDIC01B2':
        course_poster = 'https://dudic.io/wp-content/uploads/2020/05/Design_thinking.pdf'
    if course_id == 'DUDIC02B2':
        course_poster = 'https://dudic.io/wp-content/uploads/2020/05/2D-_3D-Product.pdf'
    if course_id == 'DUDIC03B2':
        course_poster = 'https://dudic.io/wp-content/uploads/2020/05/Electronics_product.pdf'
    if course_id == 'DUDIC04B2':
        course_poster = 'https://dudic.io/wp-content/uploads/2020/05/Design_innovation.pdf'
    if course_id == 'DUDIC05B2':
        course_poster = 'https://dudic.io/wp-content/uploads/2020/05/Branding_Basics.pdf'
    if course_id == 'CISE01B2':
        course_poster = 'https://dudic.io/wp-content/uploads/2020/05/Understanding_social.pdf'

    return course_poster

def rescheduling_mail(name, email):
    print(name, email)
    template = render_to_string('reshedule_mail.html', 
                            {'name' : name,})
    email = EmailMessage(
        'Electronics product Designing Course rescheduled on 23-24 May',
        template,
        settings.FROM_EMAIL,
        [email,],
        reply_to=['ask@dudic.io'],
    )
    email.content_subtype = "html"

    email.fail_silently = False
    email.send()
    if email.send():
        return True
    else:
        return False


def guideline_mail(name, email, course_name, start_date, time, guide_link):
    print(name, email)
    template = render_to_string('guidelines_mail.html', 
                        {'name'         : name,
                            'time'         : time,
                            'date'         : start_date,
                            'guide_link'   : guide_link,
                            'course_name'  : course_name,
                        })
    email = EmailMessage(
        'Guidelines for Course Portal',
        template,
        settings.FROM_EMAIL,
        [email,],
        reply_to=['ask@dudic.io'],
    )
    email.content_subtype = "html"

    email.fail_silently = False
    email.send()
    if email.send():
        return True
    else:
        return False



def send_timing_mail(name, email, course_name, course_id, start_date, time, slack_link):
    print(name, email)
    course_poster = get_poster_link(course_id)
    template = render_to_string('timing_mail.html', 
                            {'name'         : name,
                             'time'         : time,
                             'date'         : start_date,
                             'slack_link'   : slack_link,
                             'course_poster': course_poster,
                             'course_name'  : course_name,
                            })
    email = EmailMessage(
        'Timing and Slack link for course',
        template,
        settings.FROM_EMAIL,
        [email,],
        reply_to=['ask@dudic.io'],
    )
    email.content_subtype = "html"

    email.fail_silently = False
    email.send()
    if email.send():
        return True
    else:
        return False

def send_username_password_email(username, password, 
                                email, name, course_name, 
                                start_date, end_date, course_id):
    print(username, password, email, name, course_name, start_date, end_date, course_id)
    course_poster = get_poster_link(course_id)
    
    template = render_to_string('send_username_password_email.html', 
                                {'name'       : name,
                                 'course_name': course_name,
                                 'course_id'  : course_id,
                                 'start_date' : start_date,
                                 'end_date'   : end_date, 
                                 'course_poster' : course_poster,
                                 'username' : username,
                                 'password' : password,})
    
    email = EmailMessage(
        'Username and Password for Course DIC',
        template,
        settings.FROM_EMAIL,
        [email,],
        reply_to=['ask@dudic.io'],
    )
    email.content_subtype = "html"

    email.fail_silently = False
    email.send()
    if email.send():
        return True
    else:
        return False


def success(request ,name, email, course_name, start_date, end_date, course_id):
    """After Successful Registeration"""
    print(name, email, course_name, start_date, end_date )

    course_poster = get_poster_link(course_id)

    template = render_to_string('email_template.html', 
                                {'name'       : name,
                                 'course_name': course_name,
                                 'course_id'  : course_id,
                                 'start_date' : start_date,
                                 'end_date'   : end_date, 
                                 'course_poster' : course_poster})
    email = EmailMessage(
        'Registeration Sucessful',
        template,
        settings.FROM_EMAIL,
        [email,],
        reply_to=['ask@dudic.io'],
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


### CUSTOM FUNCTIONS > GENERATE USER & PASSWORD FROM APPLICANTS
"""Refer to User fields docs
https://docs.djangoproject.com/en/3.0/topics/auth/default/
"""


import random
import uuid
import time

def password_generator(age):
    chrs = '0123456789@$#_'
    age = str(age)
    password = age.join(random.sample(chrs, k=3))
    return password

def username_generator(firstname, age):
    username = firstname + str(age)
    random_number = uuid.uuid4().hex[:2]
    username = username + str(random_number)
    return username

# add course_date for finding exact users
# ApplicationModel.objects.filter(course_name__name=courseName).filter(course_date__start_date='2020-05-19').count()
# ApplicationModel.objects.filter(course_name__name=courseName).filter(course_date__start_date='2020-05-19').filter(email_sent=False)

check = []

def create_user(courseName, courseStartDate):
    # import pdb;pdb.set_trace()
    # total = ApplicationModel.objects.filter(course_name__name=courseName).filter(course_date__start_date=courseStartDate).count()
    total = ApplicationModel.objects.filter(course_name__name=courseName).filter(course_date__start_date=courseStartDate).filter(email_sent=False).count()
    print(total)
    qs = ApplicationModel.objects.filter(course_name__name=courseName).filter(course_date__start_date=courseStartDate).filter(email_sent=False)
    # qs = ApplicationModel.objects.filter(course_name__name=courseName).filter(course_date__start_date=courseStartDate).filter(email_sent=False)
    # qs = ApplicationModel.objects.filter(course_name__name=courseName)
    for user in qs:
        name = user.name
        firstname = name.split()[0]
        age = user.age
        username = username_generator(firstname, age)
        print(username)
        password = str(password_generator(age))
        print(password)
        email = user.email
        course_name = user.course_name
        start_date = user.course_date.start_date
        end_date = user.course_date.end_date
        course_id = user.course_name.id
        user_save_qs = system_user.objects.create_user(username, email, password)
        if user_save_qs:
            user.firstname = firstname
            print("user created successful {}".format(firstname))
            user.save()
            email_sent = send_username_password_email(username, password, 
                                email, name, course_name, 
                                start_date, end_date, course_id)
            if email_sent:
                applicant = ApplicationModel.objects.filter(course_name__name=courseName).filter(name=user)
                applicant.update(email_sent=True)
                UserModel.objects.create(username=username, email=email, password=password, course_name=course_name)
                print('User Created')
                # print('Will Wait for 500 seconds')
                # time.sleep(100)
            print('reached')
        else:
            print('user not created')
            check.append(firstname)

# applicant = ApplicationModel.objects.filter(course_name__name=courseName).filter(name=user)
# applicant.delete()

# UserModel.objects.create(username=username, email=email, password=password, course_name=course_name, date=date)
# print('User Created')

# def course_time():
#     time = ''
#     slack_link = ''

def timing_mail(courseName, courseStartDate):
    # total = ApplicationModel.objects.filter(course_name__name=courseName).filter(course_date__start_date=courseStartDate).filter(email_sent=True).count()
    total = ApplicationModel.objects.filter(course_name__name=courseName).filter(course_date__start_date=courseStartDate).count()
    # print(total)
    # qs = ApplicationModel.objects.filter(course_name__name=courseName).filter(course_date__start_date=courseStartDate).filter(email_sent=True)
    qs = ApplicationModel.objects.filter(course_name__name=courseName).filter(course_date__start_date=courseStartDate)
    # qs = ApplicationModel.objects.filter(course_name__name=courseName).filter(course_date__start_date=courseStartDate).filter(name='testworld')
    for user in qs:
        name = user.name
        email = user.email
        course_name = user.course_name
        course_id = user.course_name.id
        start_date = user.course_date.start_date
        time = '11 AM'
        slack_link = 'https://join.slack.com/t/dis-3sg7195/shared_invite/zt-ercfq9ur-pY6yzRUJAACVM~Dx7dnLYQ'
        from_email = 'course@dudic.io'
        email_sent = send_timing_mail(name, email, course_name,course_id, start_date, time, slack_link)
        if email_sent:
            print('email sent to {} on {}'.format(name,email))
            # print('Will Wait for 100 seconds')
            # time.sleep(100)
        else:
            print('email failed of {} on {}'.format(name,email))

def rescheduling_mail_func(courseName, courseStartDate):
    # total = ApplicationModel.objects.filter(course_name__name=courseName).filter(course_date__start_date=courseStartDate).filter(email_sent=True).count()
    total = ApplicationModel.objects.filter(course_name__name=courseName).filter(course_date__start_date=courseStartDate).count()
    print(total)
    # qs = ApplicationModel.objects.filter(course_name__name=courseName).filter(course_date__start_date=courseStartDate).filter(email_sent=True)
    qs = ApplicationModel.objects.filter(course_name__name=courseName).filter(course_date__start_date=courseStartDate)
    for user in qs:
        name = user.name
        email = user.email
        from_email = 'course@dudic.io'
        email_sent = rescheduling_mail(name, email)
        if email_sent:
            print('email sent to {} on {}'.format(name,email))
            # print('Will Wait for 100 seconds')
            # time.sleep(100)
        else:
            print('email failed of {} on {}'.format(name,email))


def guidelines_mail_func(courseName, courseStartDate):
    total = ApplicationModel.objects.filter(course_name__name=courseName).filter(course_date__start_date=courseStartDate).count()
    #qs = ApplicationModel.objects.filter(course_name__name=courseName).filter(course_date__start_date=courseStartDate)
    qs = ApplicationModel.objects.filter(course_name__name=courseName).filter(course_date__start_date=courseStartDate)
    for user in qs:
        name = user.name
        email = user.email
        course_name = user.course_name
        course_id = user.course_name.id
        start_date = user.course_date.start_date
        time = '10 AM'
        guide_link = 'https://dudic.io/wp-content/uploads/2020/05/Guide-to-portal-1.pdf'
        from_email = 'course@dudic.io'
        email_sent = guideline_mail(name, email, course_name, start_date, time, guide_link)
        if email_sent:
            print('email sent to {} on {}'.format(name,email))
            # print('Will Wait for 100 seconds')
            # time.sleep(100)
        else:
            print('email failed of {} on {}'.format(name,email))


from login.models import *
def test_mailr():
    courseName = 'Branding Basics'
    courseStartDate = '2020-05-26'
    timing_mail(courseName, courseStartDate)

# import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

# def test_sendGrid_mail():
#     message = Mail(
#         from_email='coursel@dudic.io',
#         to_emails='pradyumg@gmail.com',
#         subject='Sending with Twilio SendGrid is Fun',
#         html_content='<strong>and easy to do anywhere, even with Python</strong>',
#     )

#     sg = SendGridAPIClient('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')
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
#     # except Exception as e:
#     #     print(e.message)




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

####################### LOGIN ###########################
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages

def login_page(request):
    """login page for user login"""
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('login:course_page')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'login_page.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home_page')

####################### LOGOUT USER ###########################















































###############################################################
    



