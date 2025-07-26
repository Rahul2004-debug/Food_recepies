from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()
    
    
class Car(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    
    def __str__ (self):
        return f'{self.name} - {self.price}'
    