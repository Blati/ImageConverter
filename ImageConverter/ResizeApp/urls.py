from django.urls import path

from ResizeApp.views import home_view, upload_image

urlpatterns = [
    path('', home_view, name='home'),
    path('add/', upload_image, name='add'),
]
