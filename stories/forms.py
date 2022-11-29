from django import forms
from .models import Story

class AddPostForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = ("title","image", "story", "anonymus")
