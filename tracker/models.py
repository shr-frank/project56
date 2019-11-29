from django.db import models
class Squirrel(models.Model):
    latitude=models.FloatField()
    longitude=models.FloatField()
    unique_squirrel_id=models.CharField(max_length=20)
    shift=models.CharField(max_length=5)
    date=models.DateField()
    age=models.CharField(max_length=20,null=True)
    primary_fur_color=models.CharField(max_length=20,null=True)
    location=models.CharField(max_length=20,null=True)
    specific_location=models.CharField(max_length=100,null=True)
    running=models.BooleanField()
    chasing=models.BooleanField()
    climbing=models.BooleanField()
    eating=models.BooleanField()
    foraging=models.BooleanField()
    other_activities=models.CharField(max_length=20,null=True)
    kuks=models.BooleanField()
    quaas=models.BooleanField()
    moans=models.BooleanField()
    tail_flags=models.BooleanField()
    tail_twiches=models.BooleanField()
    approaches=models.BooleanField()
    indifferent=models.BooleanField()
    runs_from=models.BooleanField()
    def __str__(self):
        return f'Squirrel: {self.unique_squirrel_id}'

# Create your models here.
