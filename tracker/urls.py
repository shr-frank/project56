from django.urls import path

from . import views

urlpatterns = [
    path('sightings/', views.sightings,  name='sightings.html'),
    path('<str:unique_squirrel_id>/',views.update,name='update')
]
