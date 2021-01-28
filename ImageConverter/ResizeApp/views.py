from django.shortcuts import render

from ResizeApp.models import Image


def home_view(request):
    if request.method == 'GET':
        data = Image.objects.all()
        return render(request,
                      'home.html',
                      {'data': data})

