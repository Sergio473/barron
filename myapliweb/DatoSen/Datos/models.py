from tabnanny import verbose
from django.db import models

class Dato(models.Model):
    nameSen= models.CharField('nombreSensor', max_length=20,    
    )
    Fecha=models.DateField(blank=True, null=True
    )
    valor=models.CharField('valorSensor', max_length=6,    
    )

class Meta:
    verbose_name = 'Dato'
    verbose_name = 'Datos'

    def __str__(self):
        return self.nameSen 