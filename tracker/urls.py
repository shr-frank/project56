from django.urls import path

from . import views

urlpatterns = [
    path('sightings/', views.sightings,  name='sightings.html'),
]
