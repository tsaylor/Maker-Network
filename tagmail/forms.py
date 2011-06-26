from django import forms
from taggit.forms import TagField

class NewThreadForm(forms.Form):
    subject = forms.CharField(max_length=255)
    tags = TagField(help_text="A comma-separated list of tags.")
    body = forms.CharField()

