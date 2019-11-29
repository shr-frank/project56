from django.shortcuts import render
from django.template import RequestContext
from .models import *
from .module import *
from django.apps import apps
def sightings(request):
    sq_all=Squirrel.objects.all()
    return render(request, 'tracker/sightings.html', locals())
def update(request,unique_squirrel_id):
    
    if request.method=='POST':
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
    

# Create your views here.
