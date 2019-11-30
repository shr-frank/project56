from django.shortcuts import render
from django.template import RequestContext
from .models import *
from django.apps import apps
from tracker.models import Squirrel

def map(request):
    return(render(request, 'tracker/map.html',locals()))
def sightings(request):
    sq_all=Squirrel.objects.all()
    return render(request, 'tracker/sightings.html', locals())

def update(request,unique_squirrel_id):
    if request.method=='POST' and len(list(request.POST.values()))==1:
        print('Successfully Deleted Squirrel')
        sqs = Squirrel.objects.filter(unique_squirrel_id=unique_squirrel_id)
        for sq in sqs:
            sq.delete()

    elif  request.method=='POST':
        print('Successfully Updated Squirrel')
        x=list(request.POST.values())[1:]
        sqs = Squirrel.objects.filter(unique_squirrel_id=unique_squirrel_id)
        model = apps.get_model('tracker', 'Squirrel')
        field_names = [f.name for f in model._meta.fields][1:]
        for sq in sqs:
            for idx,f in enumerate(field_names):
                if x[idx]:
                    setattr(sq,f,x[idx])
            sq.save()
    return render(request, 'tracker/update.html',locals())

def add(request):
    if request.method=='POST':
        x=list(request.POST.values())[1:]
        x=[item if item else None for item in x]
        q = Squirrel(latitude=x[0],\
             longitude=x[1],\
             unique_squirrel_id=x[2],\
             shift=x[3],\
             date=x[4],\
             age=x[5],\
             primary_fur_color=x[6],\
             location=x[7],\
             specific_location=x[8],\
             running=x[9],\
             chasing=x[10],\
             climbing=x[11],\
             eating=x[12],\
             foraging=x[13],\
             other_activities=x[14],\
             kuks=x[15],\
             quaas=x[16],\
             moans=x[17],\
             tail_flags=x[18],\
             tail_twiches=x[19],\
             approaches=x[20],\
             indifferent=x[21],\
             runs_from=x[22])
        q.save()
        print('successully added a new squirrel')
    return render(request, 'tracker/add.html',locals())

# Create your views here.
