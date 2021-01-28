from django.urls import path

from ResizeApp.views import home_view, upload_image, image_detail

urlpatterns = [
    path('', home_view, name='home'),
    path('add/', upload_image, name='add'),
    path('<str:img_name>/', image_detail, name='image-detail'),
]
