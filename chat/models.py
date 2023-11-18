from django.db import models


class Mensaje(models.Model):
    mensaje = models.CharField(max_length=200)
    destinatario = models.CharField(max_length=30)
    emisor = models.CharField(max_length=30)
    
    
    def __str__(self):
        return f'{self.emisor} - {self.mensaje} - {self.destinatario}'




# Create your models here.
