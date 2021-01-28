from django.urls import path

from ResizeApp.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
]
