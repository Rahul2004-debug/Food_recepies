from django.db import models

# Create your models here.


class Recepies(models.Model):
    recepies_name=models.CharField(max_length=100,db_index=True)
    recepies_description=models.TextField()
    recepies_image=models.ImageField(upload_to='recepie_images/')