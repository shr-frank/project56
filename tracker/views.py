from django.shortcuts import render
from .models import *
def sightings(request):
    sq_all=Squirrel.objects.all()
    return render(request, 'tracker/sightings.html', locals())


# Create your views here.
