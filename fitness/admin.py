from django.contrib import admin
from .models import Fitness, Image, Lesson, Course, Home

from tinymce.widgets import TinyMCE
from django.db import models

class CourseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

class LessonAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

class HomeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.register(Fitness)
admin.site.register(Image)