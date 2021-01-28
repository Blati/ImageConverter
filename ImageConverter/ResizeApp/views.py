from django.contrib import messages
from django.shortcuts import render, redirect

from ResizeApp.forms import ImageForm
from ResizeApp.models import Image


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            if not form.cleaned_data['link'] and not form.cleaned_data['image']:
                messages.add_message(request,
                                     messages.ERROR,
                                     "Введите хотя бы одно поле!")
                return redirect('/')
            if form.cleaned_data['link'] and form.cleaned_data['image']:
                messages.add_message(request,
                                     messages.ERROR,
                                     "Введите хотя бы одно поле!")
                return redirect('/')
            form.save()
            return redirect('/')
    else:
        form = ImageForm()
    return render(request,
                  'add.html',
                  {'form': form})


def home_view(request):
    if request.method == 'GET':
        data = Image.objects.all()
        return render(request,
                      'home.html',
                      {'data': data})

