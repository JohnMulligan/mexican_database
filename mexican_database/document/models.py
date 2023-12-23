from django.db import models
from geo.models import Lugar
from django.core.validators import MaxValueValidator, MinValueValidator


	
class Archivo(models.Model):
	
	lugar = models.ForeignKey(
		Lugar,
		verbose_name="Lugar de Archivo",
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='archivos'
	)
	
	archivo=models.CharField(
		"Nombre de Archivo",
		max_length=150,
		unique=True,
		null=False,
		blank=False
	)
	
	def __str__(self):
		return self.archivo

	
class Fondo(models.Model):
	
	fondo=models.CharField(
		max_length=150,
		null=False,
		blank=False
	)
	
	archivo = models.ForeignKey(
		Archivo,
		verbose_name="Archivo",
		null=False,
		blank=False,
		on_delete=models.CASCADE,
		related_name='fondos'
	)
	
	def __str__(self):
		return self.fondo


class SubFondo(models.Model):

	subfondo=models.CharField(
		max_length=150,
		null=False,
		blank=False
	)
	
	fondo = models.ForeignKey(
		Fondo,
		verbose_name="Fondos",
		null=False,
		blank=False,
		on_delete=models.CASCADE,
		related_name='subfondos'
	)
	
	def __str__(self):
		return self.subfondo


class Volumen(models.Model):

	volumen=models.CharField(
		max_length=150,
		null=False,
		blank=False
	)
	
	subfondo = models.ForeignKey(
		SubFondo,
		verbose_name="SubFondo",
		null=False,
		blank=False,
		on_delete=models.CASCADE,
		related_name='subfondos'
	)
	
	def __str__(self):
		return self.volumen


class Asunto(models.Model):
	
	nombre = models.CharField(
		"Name of Document Type",
		max_length=255,
		unique=True
	)
	
	def __str__(self):
		return self.nombre


class Documento(models.Model):
	
	dia = models.IntegerField(
		null=True,
		blank=True,
		validators=[MinValueValidator(1),MaxValueValidator(31)]
	)
	
	mes = models.IntegerField(
		null=True,
		blank=True,
		validators=[MinValueValidator(1),MaxValueValidator(12)]
	)
	
	ano = models.IntegerField(
		null=True,
		blank=True,
		validators=[MinValueValidator(0),MaxValueValidator(2000)]
	)
	
	fuente_folio=models.CharField(
		max_length=50,
		null=True,
		blank=True
	)
	
	volumen=models.ForeignKey(
		Volumen,
		null=False,
		blank=False,
		on_delete=models.CASCADE,
	)
	
	resumen=models.CharField(
		max_length=250,
		null=True,
		blank=True
	)
	
	asunto=models.ForeignKey(
		Asunto,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	
	evento_valor=models.CharField(
		max_length=50,
		null=True,
		blank=True
	)
	
	evento_forma_de_pago=models.CharField(
		max_length=50,
		null=True,
		blank=True
	)
	
	evento_total=models.CharField(
		max_length=50,
		null=True,
		blank=True
	)