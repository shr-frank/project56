from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path('sightings/', views.sightings,  name='sightings.html'),
    path('<str:unique_squirrel_id>/',views.update,name='update')
]
