from django.contrib import admin
from .models import *

# class lectureInline(admin.StackedInline):
#     model = lecture
#     extra = 1

class lectureInline(admin.TabularInline):
    model = lecture
    extra = 0
    can_delete = True

class CourseAdmin(admin.ModelAdmin):
    inlines = [lectureInline]

admin.site.register(Course, CourseAdmin)

# admin.site.register(Course)
# admin.site.register(lecture)

