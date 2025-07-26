from django import forms
from tinymce.widgets import TinyMCE
from . import models

class CustomForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={
        'cols': 80, 
        'rows': 50,
    }, mce_attrs={
        'plugins': 'code table',  # Add 'table' plugin
        'toolbar': 'undo redo | styleselect | bold italic | code',  # Include code plugin in toolbar
        'valid_elements': '*[*]',  # Allow all elements and attributes
        'entity_encoding': 'raw',  # Prevent encoding of HTML entities
        'extended_valid_elements': (
            'table[border|cellpadding|cellspacing],thead,tbody,tr,th,td,'  # Extended valid table elements
            'p,div,span,img[src|alt|width|height],a[href|target]'  # Allow other useful elements like images, links
        ),
        'menubar': False,  # Set to False or True depending on preference
    }))

    class Meta:
        model = models.Post
        fields = ("title", "body", "slug", "banner")

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        super().__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if models.Post.objects.filter(title=title, author=self.author).exists():
            raise forms.ValidationError("A post with this title already exists.")
        return title
