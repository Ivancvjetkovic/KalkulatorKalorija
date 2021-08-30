from django.db import models
from django.contrib.auth.models import User


class Tabla(models.Model):
    ime=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return str(self.ime)



class Namirnica(models.Model):
    naziv = models.CharField(max_length=200)
    ugljikohidrati = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    masnoca = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    proteini = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    kalorije=models.DecimalField(max_digits=5,decimal_places=2,default=0,blank=True)
    
    def __str__(self):
        return str(self.naziv)

class RelacijaTablaNamirnica(models.Model):
    tablica = models.ManyToManyField(Tabla,blank=True)
    namirnica = models.ManyToManyField(Namirnica)
    