from django.urls import path

from . import views

urlpatterns = [
    path('', views.sample,  name='sample.html'),
]
