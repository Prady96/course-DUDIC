from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class CourseModel(models.Model):
    """ Name and Id for each course conducting under DUDIC """
    
    id = models.CharField(
        primary_key=True,
        max_length=10
    )
    name = models.CharField(
        max_length = 100,
        unique = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class DateModel(models.Model):
    """ Each Course can have many Dates """

    start_date = models.DateField()
    end_date = models.DateField(null=True)
    course_id = models.ForeignKey(
        CourseModel, 
        on_delete = models.SET_NULL, 
        null = True, 
        blank = False,
        related_name ='relateds' 
    )
    registeration = models.IntegerField()

    closed_at = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.start_date, self.end_date)

    class Meta:
        verbose_name = 'Date'
        verbose_name_plural = 'Dates'


class ApplicationModel(models.Model):
    """ All the User Applied on Portal """

    name               = models.CharField(max_length=50)
    education          = models.CharField(max_length=50)
    age                = models.IntegerField()
    address            = models.CharField(max_length=200)
    mobile_num         = PhoneNumberField()
    email              = models.EmailField()
    reason             = models.CharField(max_length=500)
    instituteOrStartup = models.CharField(max_length=200, null=True)
    student_details    = models.CharField(max_length=100)
    hear_about         = models.CharField(max_length=100)
    course_name        = models.ForeignKey(CourseModel, 
        on_delete = models.SET_NULL, 
        null = True, 
        blank = False,
    )
    course_date = models.ForeignKey(
        DateModel, 
        on_delete=models.SET_NULL, 
        null = True, 
        blank = False,
        related_name = 'relateds'
    )

    enable_certificate = models.BooleanField(default=False)

    CERTIFICATE_GRADE =  (
        ('VGD', 'Very Good'),
        ('GOD', 'Good'),
        ('SAT', 'Satisfactory'),
        ('EXE', 'Excellent'),
        ('NVA', 'Not Valid'),
    )

    certificate_grade = models.CharField(max_length=3, choices = CERTIFICATE_GRADE, default='NVA')

    date  = models.DateField(auto_now=True)

    email_sent = models.BooleanField(default = False)

    timing_mail_sent = models.BooleanField(default = False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'


from django.conf import settings

User = settings.AUTH_USER_MODEL


class UserModel(models.Model):
    """ Selected User After Application """
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100, null=True)
    course_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Selected User'
        verbose_name_plural = 'Selected Users'

class certificates_list(models.Model):
    """ list of students for which
     certificates will be created """

    name = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    date = models.DateField()
    
    CERTIFICATE_GRADE =  (
        ('VGD', 'Very Good'),
        ('GOD', 'Good'),
        ('SAT', 'Satisfactory'),
        ('EXE', 'Excellent'),
        ('NVA', 'Not Valid'),
    )
    
    certificate_grade = models.CharField(max_length=3, choices = CERTIFICATE_GRADE, default='NVA')

    email_sent = models.BooleanField(default = False)






