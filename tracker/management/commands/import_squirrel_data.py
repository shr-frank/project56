import pandas as pd
import datetime
from tracker.models import Squirrel
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **kwargs):
        x = kwargs['file']
        def todate(x):
            x=str(x)
            year=int(x[-4:])
            date=int(x[-6:-4])
            month=int(x[-8:-6])
            return datetime.date(year,month,date)
        df=pd.read_csv(x)
        df['Date']=df['Date'].apply(todate)

        for idx in range(len(df)):
            q = Squirrel(latitude=df.loc[idx,'Y'],\
                         longitude=df.loc[idx,'X'],\
                         unique_squirrel_id=df.loc[idx,'Unique Squirrel ID'],\
                         shift=df.loc[idx,'Shift'],\
                         date=df.loc[idx,'Date'],\
                         age=df.loc[idx,'Age'],\
                         primary_fur_color=df.loc[idx,'Primary Fur Color'],\
                         location=df.loc[idx,'Location'],\
                         specific_location=df.loc[idx,'Specific Location'],\
                         running=df.loc[idx,'Running'],\
                         chasing=df.loc[idx,'Chasing'],\
                         climbing=df.loc[idx,'Climbing'],\
                         eating=df.loc[idx,'Eating'],\
                         foraging=df.loc[idx,'Foraging'],\
                         other_activities=df.loc[idx,'Other Activities'],\
                         kuks=df.loc[idx,'Kuks'],\
                         quaas=df.loc[idx,'Quaas'],\
                         moans=df.loc[idx,'Moans'],\
                         tail_flags=df.loc[idx,'Tail flags'],\
                         tail_twiches=df.loc[idx,'Tail twitches'],\
                         approaches=df.loc[idx,'Approaches'],\
                         indifferent=df.loc[idx,'Indifferent'],\
                         runs_from=df.loc[idx,'Runs from'])
            q.save()
