from django.contrib import admin
from .models import Repuesto,Categoria
from tinymce.widgets import TinyMCE
from django.db import models
"""
class CategoriaAdmin(admin.ModelAdmin):
    fields=[
            'nombre',
            'descripcion'          
        ]
    
    formfield_overrides={
        models.TextField:{'widget': TinyMCE()}
    }
    
class RepuestoAdmin(admin.ModelAdmin):
    fields=[
            'nombre',
            'precio',
            'categoria',
            'imagen',
            'descripcion'          
        ]

  #  fieldsets = [
   #     ("Nombre/Precio/Fecha", {"fields": ["nombre","precio","fecha_publicacion"]}),
   #     ("Descripcion", {"fields": ["descripcion"]})
   # ]
    
    formfield_overrides={
        models.TextField:{'widget': TinyMCE()}
    }
"""
admin.site.register(Categoria)
admin.site.register(Repuesto)
