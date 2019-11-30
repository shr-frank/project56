from django.urls import path

from . import views

urlpatterns = [
    path('sightings/add/', views.add, name='add'),
    path('sightings/', views.sightings,  name='sightings.html'),
    path('map/',views.map,name='map'),
    path('<str:unique_squirrel_id>/',views.update,name='update')
]
