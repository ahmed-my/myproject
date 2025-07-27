from django.contrib import admin
from .models import HeroPhrase

@admin.register(HeroPhrase)
class HeroPhraseAdmin(admin.ModelAdmin):
    list_display = ['text']
    search_fields = ['text']
