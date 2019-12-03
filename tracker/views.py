from django.shortcuts import render
from django.template import RequestContext
from .models import *
from django.apps import apps
from django.db import connection

def map(request):
    sqs=Squirrel.objects.raw('SELECT id, latitude, longitude,unique_squirrel_id from tracker_squirrel')
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
             tail_twitches=x[19],\
             approaches=x[20],\
             indifferent=x[21],\
             runs_from=x[22])
        q.save()
        print('successully added a new squirrel')
    return render(request, 'tracker/add.html',locals())

def stats(request):
    cursor = connection.cursor()
    query="""select count(*) as total_sightings,sum(running) as running_squirrels,sum(chasing) as chasing_squirrels,
          sum(eating)as eating_squirrels,sum(foraging) as foraging_squirrels,
          sum(kuks) as kuks, sum(quaas) as quaas,
          sum(tail_flags) as tail_flags,sum(tail_twitches) as tail_twitches
             from tracker_squirrel """
    cursor.execute(query)
    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]
    result = cursor.fetchone()
    dict_1=dict()
    for idx in range(len(field_names)):
        dict_1[field_names[idx]]=result[idx]

    cursor = connection.cursor()
    query="""select primary_fur_color,count(*)
             from tracker_squirrel
             group by primary_fur_color"""
    cursor.execute(query)
    result = cursor.fetchall()
    dict_2=dict()
    for idx in range(len(result)):
        dict_2[result[idx][0]]=result[idx][1]
    del dict_2['nan']

    cursor = connection.cursor()
    query="""select age,count(*)
             from tracker_squirrel
             group by age"""
    cursor.execute(query)
    result = cursor.fetchall()
    dict_3=dict()
    for idx in range(len(result)):
        dict_3[result[idx][0]]=result[idx][1]
    del dict_3['?']
    del dict_3['nan']
    return render(request, 'tracker/stats.html',locals())


