from django.db import models
from geo.models import Location
from django.core.validators import MaxValueValidator, MinValueValidator


	
class Archivo(models.Model):
	location = models.ForeignKey(
		Location,
		verbose_name="Archive Location",
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='archives'
	)
	name=models.CharField(
		"Archive name",
		max_length=20,
		unique=True,
		null=True,
		blank=True
	)
	def __str__(self):
		return self.name

	
class Fondo(models.Model):
	archivo = models.ForeignKey(
		Archivo,
		verbose_name="Archivo",
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='fondos'
	)


class SubFondo(models.Model):
	fondo = models.ForeignKey(
		Fondo,
		verbose_name="Fondo",
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='subfondos'
	)




class Volume(models.Model):
	parent = models.ForeignKey(
		'self',
		verbose_name="Child of",
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='children'
	)


class Asunto(models.Model):
	"""
		Document Type
	"""

	nombre = models.CharField(
		"Geographic Location Type",
		max_length=255,
		unique=True
	)
	def __str__(self):
		return self.name


class Documento(models.Model):
	
	day = models.IntegerField(
		null=True,
		blank=True,
		validators=[MinValueValidator(1),MaxValueValidator(31)]
	)
	month = models.IntegerField(
		null=True,
		blank=True,
		validators=[MinValueValidator(1),MaxValueValidator(12)]
	)
	year = models.IntegerField(
		null=True,
		blank=True,
		validators=[MinValueValidator(0),MaxValueValidator(2000)]
	)
	
	folio=models.CharField(
		"Folio",
		max_length=50,
		unique=True,
		null=True,
		blank=True
	)
	vol=models.CharField(
		"volume",
		max_length=50,
		unique=True,
		null=True,
		blank=True
	)
	resumen=models.CharField(
		"Resumen",
		max_length=250,
		unique=False,
		null=True,
		blank=True
	)