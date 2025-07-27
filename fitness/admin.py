from django.contrib import admin
from django.db import models
from .models import Fitness, Image, Lesson, Course, Home, Article, Tip, Quote, HeroPhrase, LeadMagnet, AffiliateTool, Tool, ToolClick
from tinymce.widgets import TinyMCE


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

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_featured')
    search_fields = ('name', 'description', 'category')
    list_filter = ('category', 'is_featured')

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(LeadMagnet)
admin.site.register(AffiliateTool)
admin.site.register(Home, HomeAdmin)
admin.site.register(Image)

# Register models for the fitness app
admin.site.register(Fitness)
admin.site.register(Article)
admin.site.register(Tip)
admin.site.register(Quote)

@admin.register(HeroPhrase)
class HeroPhraseAdmin(admin.ModelAdmin):
    list_display = ['text']
    search_fields = ['text']


@admin.register(ToolClick)
class ToolClickAdmin(admin.ModelAdmin):
    list_display = ('tool_name', 'click_time', 'ip_address', 'user_agent')
    list_filter = ('tool_name', 'click_time')
