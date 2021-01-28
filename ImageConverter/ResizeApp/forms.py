from django import forms

from ResizeApp.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('link', 'image',)
