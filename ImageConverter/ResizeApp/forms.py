from django import forms

from ResizeApp.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('link', 'image',)


class UserForm(forms.Form):
    width = forms.CharField(max_length=5, label='Ширина', required=False)
    height = forms.CharField(max_length=5, label='Высота', required=False)
