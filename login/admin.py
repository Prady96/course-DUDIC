from django.contrib import admin
from .models import *

admin.site.site_header = "DUDIC Courses"
admin.site.site_title = "DUDIC Admin Portal"
admin.site.index_title = "Welcome to DUDIC Courses Portal"

# admin.site.register(ApplyModel)
# admin.site.register(CourseModel)
# admin.site.register(DateModel)
# admin.site.register(ApplicationModel)
admin.site.register(UserModel)


@admin.register(CourseModel)
class CourseAdminModel(admin.ModelAdmin):
    list_display = ['name','id',]
    # list_filter = ['name', 'course_id']
    ordering = ['name',]
    save_as = True

@admin.register(ApplicationModel)
class ApplicationAdminModel(admin.ModelAdmin):
    list_display = ['name','education','age','email','reason','hear_about','course_name','course_date','date']
    list_filter = ['course_name', 'course_date']
    ordering = ['name','date']
    search_fields = ['name',]
    save_as = True


@admin.register(DateModel)
class DateCourseModel(admin.ModelAdmin):
    list_display = ['id','start_date','end_date','course_id','registeration']
    list_filter = ['start_date', 'course_id']
    ordering = ['start_date','course_id']
    save_as = True

