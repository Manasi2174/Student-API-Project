from django.db import models # type: ignore

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(unique=True,primary_key=True)
    marks = models.FloatField()
    subjects = models.CharField(max_length=255,help_text="Comma-separated subjects")

    def __str__(self):
        return f"{self.name} ({self.roll})"
    
    
