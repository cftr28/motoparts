from datetime import datetime
from django.db import models
from datetime import datetime

class Categoria(models.Model):
    nombre=models.CharField('nombre ',max_length=200, blank=False, null=False )
    descripcion=models.TextField('descripcion ',max_length=220, blank=False, null=False )
    
    def __str__(self):
        return f'{self.nombre}  {self.descripcion}'    
    
  
class Repuesto(models.Model):
    nombre=models.CharField('nombre ',max_length=200, blank=False, null=False )
    categoria=models.CharField('categoria ',max_length=200, blank=False, null=False )
    descripcion=models.TextField('descripcion ',max_length=220, blank=False, null=False )
    imagen = models.ImageField(upload_to="ImgRepuestos", null=True)
    cantidad=models.IntegerField('stock disponible: ',blank=False, null=False)
    precio=models.IntegerField('precio $ ',blank=False, null=False)
    
    def __str__(self):
        return f'{self.nombre}   {self.precio}'


    
    