from django.db import models
class Squirrel(models.Model):
    latitude=models.FloatField(null=True)
    longitude=models.FloatField(null=True)
    unique_squirrel_id=models.CharField(max_length=20,null=True)
    shift=models.CharField(max_length=5,null=True)
    date=models.DateField(null=True)
    age=models.CharField(max_length=20,null=True)
    primary_fur_color=models.CharField(max_length=20,null=True)
    location=models.CharField(max_length=20,null=True)
    specific_location=models.CharField(max_length=100,null=True)
    running=models.BooleanField(null=True)
    chasing=models.BooleanField(null=True)
    climbing=models.BooleanField(null=True)
    eating=models.BooleanField(null=True)
    foraging=models.BooleanField(null=True)
    other_activities=models.CharField(max_length=20,null=True)
    kuks=models.BooleanField(null=True)
    quaas=models.BooleanField(null=True)
    moans=models.BooleanField(null=True)
    tail_flags=models.BooleanField(null=True)
    tail_twitches=models.BooleanField(null=True)
    approaches=models.BooleanField(null=True)
    indifferent=models.BooleanField(null=True)
    runs_from=models.BooleanField(null=True)
    def __str__(self):
        return f'Squirrel: {self.unique_squirrel_id}'

# Create your models here.
