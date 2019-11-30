from django.urls import path

from . import views

urlpatterns = [
    path('sightings/stats/',views.stats, name='stats'),
    path('sightings/add/', views.add, name='add'),
    path('sightings/', views.sightings,  name='sightings'),
    path('map/',views.map,name='map'),
    path('sightings/<str:unique_squirrel_id>/',views.update,name='update')
]
