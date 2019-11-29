import datetime
from tracker.models import Squirrel
from django.core.management.base import BaseCommand
import csv

class Command(BaseCommand):
    
    args = '[appname.ModelName]'
    
    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **kwargs):
        x=kwargs['file']
        from django.apps import apps
        model = apps.get_model('tracker', 'Squirrel')
        field_names = [f.name for f in model._meta.fields]
        with open(x, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(field_names)
            for instance in model.objects.all():
                writer.writerow([getattr(instance, f) for f in field_names])
