from django.db import models
class Squirrel(models.Model):
    latitude=models.FloatField(blank=True,null=True)
    longitude=models.FloatField(blank=True,null=True)
    unique_squirrel_id=models.CharField(max_length=20,blank=True,null=True)
    shift=models.CharField(max_length=5,blank=True,null=True)
    date=models.DateField(blank=True,null=True)
    age=models.CharField(max_length=20,blank=True,null=True)
    primary_fur_color=models.CharField(max_length=20,blank=True,null=True)
    location=models.CharField(max_length=20,blank=True,null=True)
    specific_location=models.CharField(max_length=100,blank=True,null=True)
    running=models.BooleanField(blank=True,null=True)
    chasing=models.BooleanField(blank=True,null=True)
    climbing=models.BooleanField(blank=True,null=True)
    eating=models.BooleanField(blank=True,null=True)
    foraging=models.BooleanField(blank=True,null=True)
    other_activities=models.CharField(max_length=20,blank=True,null=True)
    kuks=models.BooleanField(blank=True,null=True)
    quaas=models.BooleanField(blank=True,null=True)
    moans=models.BooleanField(blank=True,null=True)
    tail_flags=models.BooleanField(blank=True,null=True)
    tail_twitches=models.BooleanField(blank=True,null=True)
    approaches=models.BooleanField(blank=True,null=True)
    indifferent=models.BooleanField(blank=True,null=True)
    runs_from=models.BooleanField(blank=True,null=True)
    def __str__(self):
        return f'Squirrel: {self.unique_squirrel_id}'

# Create your models here.
