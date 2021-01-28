from django.contrib import messages
from django.shortcuts import render, redirect

from ResizeApp.forms import ImageForm, UserForm
from ResizeApp.models import Image
from ResizeApp.utils import get_path, reformat_image


def home_view(request):
    if request.method == 'GET':
        data = Image.objects.all()
        return render(request,
                      'home.html',
                      {'data': data})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            if not form.cleaned_data['link'] and not form.cleaned_data['image']:
                messages.add_message(request,
                                     messages.ERROR,
                                     "Введите хотя бы одно поле!")
                return redirect('/add')
            if form.cleaned_data['link'] and form.cleaned_data['image']:
                messages.add_message(request,
                                     messages.ERROR,
                                     "Введите хотя бы одно поле!")
                return redirect('/add')
            print(form.cleaned_data)
            form.save()
            return redirect('/')
    else:
        form = ImageForm()
    return render(request,
                  'add.html',
                  {'form': form})


def image_detail(request, img_name):
    data = Image.objects.filter(image__endswith=img_name)[0]
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            if not form.cleaned_data['width'] and not form.cleaned_data['height']:
                messages.add_message(request,
                                     messages.ERROR,
                                     "Введите хотя бы одно поле!")
                return redirect('/' + img_name)
            path = get_path(data.image.url)
            if not reformat_image(data.image,
                                  path,
                                  form.cleaned_data['width'],
                                  form.cleaned_data['height']):
                messages.add_message(request,
                                     messages.ERROR,
                                     "Введены неверные соотношения сторон!")
                return redirect('/' + img_name)
            new_obj = Image.objects.create()
            new_obj.image = path.split('\\')[1]
            new_obj.save()
            return redirect('/' + new_obj.image.name + '/')
    else:
        form = UserForm()
    return render(request,
                  'detail.html',
                  {'data': data, 'form': form})
