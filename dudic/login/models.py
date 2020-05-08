from django.db import models

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
    mobile_num         = models.IntegerField()
    email              = models.EmailField()
    reason             = models.CharField(max_length=500)
    instituteOrStartup = models.CharField(max_length=200, null=True)
    # ENTERPRENEUR = 'ER'
    # UNDERGRADUATE = 'UG'
    # POSTGRADUATE = 'PG'
    # STUDENT_DETAILS_CHOICES = [
    #                             (ENTERPRENEUR, 'Entrepreneur'),
    #                             (UNDERGRADUATE, 'Undergraduate'),
    #                             (POSTGRADUATE, 'Postgraduate'),
    #                         ]
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
        blank = False
    )

    date  = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'


from django.conf import settings

User = settings.AUTH_USER_MODEL

class UserModel(models.Model):
    """ Selected User After Application """
    user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null = True, 
        blank = False
    )
    name = models.CharField(max_length=50)
    education   = models.CharField(max_length=50)
    age         = models.IntegerField()
    address     = models.CharField(max_length=200)
    mobile_num  = models.IntegerField()
    email       = models.EmailField()
    reason      = models.CharField(max_length=500)
    hear_about  = models.CharField(max_length=100)
    
    def __str__(self):
        pass

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'




