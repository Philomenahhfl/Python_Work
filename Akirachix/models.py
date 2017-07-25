from django.db import models
import datetime

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    course=models.CharField(max_length=30)
    description = models.TextField(default = 'Disciplined')
    registration_date=models.TextField(default = datetime.date(2017,1,1))
    
    
# class Workers(models.Model):
#     name = modelsField(max_length = 100)
#     position = modelsField(max_length = 50)
#     description = models.TextField(default = 'Hardworking') 
#     registration_date = models.DateField(default = datetime.date(2017,4,19))
#     def __unicode__(self):
#         return self.Author