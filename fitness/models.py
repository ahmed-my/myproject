from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings
from tinymce.models import HTMLField
import bleach


# Update allowed tags and attributes
allowed_tags = [
    'a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'li', 'ol', 
    'strong', 'bold', 'ul', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'img', 'span'
]
allowed_attrs = {
    'a': ['href', 'title'],
    'img': ['src', 'alt', 'width', 'height'],
    'span': ['style']
}

# Create your models here.
class Fitness(models.Model):
    name = models.CharField(max_length=75)
    address = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add this for the image below
    banner = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Tip(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Quote(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.content} - {self.author}"

class Image(models.Model):
    title = models.CharField(max_length=75)
    image = models.ImageField(upload_to='images/')
    # add this for the image below

    def __str__(self):
        return self.title
    
class Home(models.Model):
    title = models.CharField(max_length=75)
    body = HTMLField()

    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    name = models.CharField(max_length=75)
    body = HTMLField()
    slug = models.SlugField()
    banner = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("fitness:lesson_page", kwargs={"param": self.slug})

    
class Course(models.Model):
    title = models.CharField(max_length=75)
    body = HTMLField()
    slug = models.SlugField()
    banner = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("fitness:course_page", kwargs={"param": self.slug})

class LeadMagnet(models.Model):
    title = models.CharField(max_length=100)
    document = models.FileField(upload_to='lead_magnets/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AffiliateTool(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()
    description = models.TextField(blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# create table model for animation phrases
class HeroPhrase(models.Model):
    language = models.CharField(
        max_length=10,
        choices=settings.LANGUAGES,
        default='en',
        verbose_name="Language"
    )
    text = models.CharField(max_length=100)

    def __str__(self):
        return f"[{self.language}] {self.text}"

class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    link = models.URLField()
    logo = models.ImageField(upload_to='tools/', blank=True)
    category = models.CharField(max_length=50, blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# create Click Tracking for Affiliate Tools
class ToolClick(models.Model):
    tool_name = models.CharField(max_length=100)
    click_time = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.tool_name} clicked at {self.click_time}"