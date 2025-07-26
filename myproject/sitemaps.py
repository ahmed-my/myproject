# sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from fitness.models import Course, Lesson

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)

class CourseSitemap(Sitemap):
    def items(self):
        return Course.objects.all()

class LessonSitemap(Sitemap):
    def items(self):
        return Lesson.objects.all()
