from django.db import models
from login.models import *
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

class Course(models.Model):
    course_name = models.ForeignKey(
        CourseModel,
        on_delete = models.SET_NULL,
        blank = False,
        null=True,
    )

    available = models.BooleanField(default=False)

    instructor = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        blank = False,
        null= True,
        related_name ='relateds'
    )

    date = models.ForeignKey(
        DateModel,
        on_delete = models.SET_NULL,
        blank = False,
        null = True,
    )

    course_image = models.ImageField(upload_to ='BASE_DIR/static/IMG/',blank=True, null=True)

    course_title = models.CharField(max_length=30, null=True, blank=False)

    STATUS = (
        ('R','Running'),
        ('C','Completed'),
        ('P','Not Started')
    )

    slack_link = models.CharField(max_length=200, null=True, blank=True)

    course_status = models.CharField(max_length=1, choices=STATUS, default='P')

    def __str__(self):
        return '{} - {}'.format(self.course_name.name, self.date)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class lecture(models.Model):

    course_name = models.ForeignKey(
        Course,
        on_delete = models.SET_NULL,
        blank = False,
        null = True,
    )

    lecture_num = models.IntegerField(default=1, blank=True)

    title = models.CharField(max_length = 30, default = ' ', blank=True)
    description = models.TextField(default = ' ', blank=True)
    zoom_link = models.CharField(max_length = 200, null = True, blank=True)
    meeting_timing = models.TimeField(null=True, blank=True)
    download_resources = models.FileField(upload_to='static/Instructor/',null=True, blank=True)
    upload_resources = models.FileField(null = True, blank=True)
    available = models.BooleanField(default = True, blank=True)
    date = models.DateField(null=True, blank=True)


    def __str__(self):
        return 'Course Name and Date {} Title {}'.format(self.course_name,self.title)

    class Meta:
        verbose_name = 'lecture'
        verbose_name_plural = 'lectures'

























