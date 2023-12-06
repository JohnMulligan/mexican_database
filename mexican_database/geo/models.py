from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator


class Poligono(models.Model):
	
	forma=models.JSONField(
		null=True,
		blank=True
	)

class TipoDeLugar(models.Model):

	nombre = models.CharField(
		max_length=255,
		unique=True
	)
	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name = "Tipo de Lugar"
		verbose_name_plural = "Tipos de Lugares"


class Lugar(models.Model):
	uuid=models.UUIDField(default=uuid.uuid4, editable=False,null=True)

	nombre = models.CharField(
		max_length=255
	)
	longitud = models.FloatField(
		null=True,
		blank=True
	)
	latitud = models.FloatField(
		null=True,
		blank=True
	)
	
	madre = models.ForeignKey(
		'self',
		verbose_name="hijo de",
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='hijos'
	)
	
	tipo_de_lugar = models.ForeignKey(
		'TipoDeLugar',
		verbose_name="Tipos de Lugar",
		null=True,
		on_delete=models.SET_NULL,
		related_name='type_Lugar'
	)
	
	extension_espacial = models.ForeignKey(
		'Poligono',
		null=True,
		blank=True,
		on_delete=models.SET_NULL
	)
	
	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name = "Lugar"
		verbose_name_plural = "Lugares"
