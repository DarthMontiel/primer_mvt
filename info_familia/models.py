from django.db import models

# Create your models here.
class datos(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    Ult_visita = models.DateField()