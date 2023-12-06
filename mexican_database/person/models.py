from django.db import models
from document.models import Documento
from geo.models import Lugar
from django.core.validators import MaxValueValidator, MinValueValidator

class CategoriaDeOcupacion(models.Model):
	nombre = models.CharField(max_length=50,blank=False,null=False,unique=True)
	
	def __str__(self):
		return self.nombre

class Ocupacion(models.Model):
	nombre = models.CharField(max_length=50,blank=False,null=False,unique=True)
	
	def __str__(self):
		return self.nombre

class Sexo(models.Model):
	nombre = models.CharField(max_length=50,blank=False,null=False,unique=True)
	
	def __str__(self):
		return self.nombre

class Etonimo(models.Model):
	nombre = models.CharField(max_length=50,blank=False,null=False,unique=True)
	
	def __str__(self):
		return self.nombre

class CalidadDePersona(models.Model):
	nombre = models.CharField(max_length=50,blank=False,null=False,unique=True)
	
	def __str__(self):
		return self.nombre

class HispanizacionDePersona(models.Model):
	nombre = models.CharField(max_length=50,blank=False,null=False,unique=True)
	
	def __str__(self):
		return self.nombre

class EstatusDeEsclavizador(models.Model):
	nombre = models.CharField(max_length=50,blank=False,null=False,unique=True)
	
	def __str__(self):
		return self.nombre

class SituacionDeLugarDeEsclavizador(models.Model):
	nombre = models.CharField(max_length=50,blank=False,null=False,unique=True)
	
	def __str__(self):
		return self.nombre


class Esclavizador(models.Model):
	
	nombre = models.CharField(max_length=50)
	
	apellido = models.CharField(max_length=50)
	
	estatus_de_esclavizador = models.ForeignKey(
		EstatusDeEsclavizador,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	
	sexo = models.ForeignKey(
		Sexo,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	
	calidad_de_persona = models.ManyToManyField(
		CalidadDePersona
	)
	
	lugar = models.ForeignKey(
		Lugar,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
	)
	
	lugar_situacion=models.ForeignKey(
		SituacionDeLugarDeEsclavizador,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
	)
	
	ocupacion = models.ForeignKey(
		Ocupacion,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	
	categoria_de_ocupacion = models.ForeignKey(
		CategoriaDeOcupacion,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)

	def __str__(self):
		return ' : '.join([i if i is not None else '' for i in [self.nombre,self.apellido]])


class PersonaEsclavizada(models.Model):
	
	primer_nombre = models.CharField(max_length=50)
	
	apellido = models.CharField(max_length=50)
	
	nombre_y_apellido_estandarizados=models.CharField(max_length=100)
	
	calidad_de_persona = models.ManyToManyField(
		CalidadDePersona
	)
	
	cabella = models.CharField(max_length=100)
	
	ojos = models.CharField(max_length=100)
	
	marcas_corporales = models.CharField(max_length=100)
	
	registros_de_conductas_y_condiciones= models.CharField(max_length=350)
	
	ocupacion = models.ForeignKey(
		Ocupacion,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	
	categoria_de_ocupacion = models.ForeignKey(
		CategoriaDeOcupacion,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	
	hispanizacion = models.ForeignKey(
		HispanizacionDePersona,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	
	sexo = models.ForeignKey(
		Sexo,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	
	etonimo = models.ForeignKey(
		Etonimo,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
	)
	
	procedencia=models.ManyToManyField(
		Lugar
	)
	
	lugar_ultimo = models.ForeignKey(
		Lugar,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	
	lugar_nuevo = models.ForeignKey(
		Lugar,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	
	etonimo = models.ForeignKey(
		Etonimo,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
	)
	
	
	etonimo = models.ForeignKey(
		Etonimo,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
	)

	notes = models.CharField(null=True, max_length=8192,blank=True)
	
	last_updated=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nombre_y_apellido_estandarizados

class TipoDeRelacion(models.Model):

	nombre = models.CharField(
		max_length=255,
		unique=True
	)
	def __str__(self):
		return self.nombre


class RolDeRelacion(models.Model):

	nombre = models.CharField(
		max_length=255,
		unique=True
	)
	def __str__(self):
		return self.nombre


class EsclavizadorDocumentoConexion(models.Model):
	
	tipo_de_relacion=models.ForeignKey(
		TipoDeRelacion,
		null=False,
		blank=False,
		on_delete=models.CASCADE
	)
	
	rol_de_esclavizador=models.ForeignKey(
		RolDeRelacion,
		null=False,
		blank=False,
		on_delete=models.CASCADE
	)
	
	esclavizador = models.ForeignKey(
		Esclavizador,
		null=False,
		blank=False,
		on_delete=models.CASCADE,
		related_name='esclavizador_relaciones'
	)
	
	documento = models.ForeignKey(
		Documento,
		null=False,
		blank=False,
		on_delete=models.CASCADE,
		related_name='documento_eslclavizador_conexiones'
	)
	
	
	def __str__(self):
		return self.persona.nombre_y_apellido_estandarizados + " " + self.documento.resumen




class EsclavizadaDocumentoConexion(models.Model):
	
	tipo_de_relacion=models.ForeignKey(
		TipoDeRelacion,
		null=False,
		blank=False,
		on_delete=models.CASCADE
	)
	
	persona_esclavizada = models.ForeignKey(
		PersonaEsclavizada,
		null=False,
		blank=False,
		on_delete=models.CASCADE,
		related_name='persona_esclavizadas_relaciones'
	)
	
	persona_edad = models.FloatField(
		"Edad registrada en el documento",
		null=True,
		blank=True
	)
	
	persona_altura = models.FloatField(
		"Altura registrada en el documento",
		null=True,
		blank=True
	)
	
	documento = models.ForeignKey(
		Documento,
		null=False,
		blank=False,
		on_delete=models.CASCADE,
		related_name='documento_esclavizada_conexiones'
	)
	
	
	def __str__(self):
		return self.persona.nombre_y_apellido_estandarizados + " " + self.documento.resumen

