from django.db import models
from ckeditor.fields import RichTextField



class Criticas(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    critica = RichTextField()
    fecha_creacion = models.DateField()
    imglibro = models.ImageField(upload_to='imagen', null=True, blank=True)
    
    def __str__(self):
        return f'{self.id} - {self.titulo} - {self.autor} - {self.fecha_creacion}'


# Create your models here.
