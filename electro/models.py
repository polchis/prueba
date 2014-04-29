from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Informacion(models.Model):
	Titulo=models.CharField(max_length=100)
	Descripcion=models.TextField(max_length=400)
	Direccion=models.CharField(max_length=100)
	imagen1 = models.ImageField(upload_to='fotos', verbose_name='imagen1')
	imagen2 = models.ImageField(upload_to='fotos', verbose_name='imagen2')
	

	def __unicode__(self):
		return self.Titulo
		 