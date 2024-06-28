from django.db import models

# Create your models here.

class studentModel(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    father_Name = models.CharField(max_length=30)
    address = models.TextField()
    
    def __str__(self):
        return f"Name:{self.name} ROll:{self.roll}"
    
    