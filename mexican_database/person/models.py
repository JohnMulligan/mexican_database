from django.db import models
from document.models import Documento
from geo.models import Location
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Occupation(models.Model):
	name = models.CharField(max_length=255,blank=False,null=False,unique=True)
	
	def __str__(self):
		return self.name

class Person(models.Model):
	
	principal_alias = models.CharField(max_length=255)
	# Personal info.
	birth_place = models.ForeignKey(
		Location,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	birth_day = models.IntegerField(
		null=True,
		blank=True,
		validators=[MinValueValidator(1),MaxValueValidator(31)]
	)
	birth_month = models.IntegerField(
		null=True,
		blank=True,
		validators=[MinValueValidator(1),MaxValueValidator(12)]
	)
	birth_year = models.IntegerField(
		null=True,
		blank=True,
		validators=[MinValueValidator(0),MaxValueValidator(2000)]
	)
	
	occupation = models.ForeignKey(
		Occupation,
		null=False,
		blank=False,
		on_delete=models.CASCADE,
		related_name='+'
	)
	
	
	death_day = models.IntegerField(
		null=True,
		blank=True,
		validators=[MinValueValidator(1),MaxValueValidator(31)]
	)
	death_month = models.IntegerField(
		null=True,
		blank=True,
		validators=[MinValueValidator(1),MaxValueValidator(12)]
	)
	death_year = models.IntegerField(
		null=True,
		blank=True,
		validators=[MinValueValidator(0),MaxValueValidator(2000)]
	)

	death_place = models.ForeignKey(
		Location,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)

	principal_location = models.ForeignKey(
		Location,
		null=True,
		on_delete=models.SET_NULL,
		db_index=True,
		blank=True,
		related_name='+'
	)
	notes = models.CharField(null=True, max_length=8192,blank=True)
	is_natural_person = models.BooleanField(null=False, default=True,blank=True)
	last_updated=models.DateTimeField(auto_now=True)
	human_reviewed=models.BooleanField(default=False,blank=True,null=True)
	#It's going to be hairy mapping all this data over from legacy
	#so I'm going to have to maintain a sort of shadow pk for use in migrations
	legacy_id=models.IntegerField(null=True,blank=True)

	def __str__(self):
		return self.principal_alias

class Alias(models.Model):
	alias = models.CharField(max_length=255)
	identity = models.ForeignKey(
		Person,
		null=False,
		blank=False,
		on_delete=models.CASCADE,
		related_name='aliases'
	)
	def __str__(self):
		return self.alias

class EnslavementRelationType(models.Model):

	name = models.CharField(
		max_length=255,
		unique=True
	)
	def __str__(self):
		return self.name


class EnslavementRelationRole(models.Model):

	name = models.CharField(
		max_length=255,
		unique=True
	)
	def __str__(self):
		return self.name

class EnslavementRelation(models.Model):
	
	relation_type=models.ForeignKey(
		EnslavementRelationType,
		null=False,
		blank=False,
		on_delete=models.CASCADE,
		related_name='person_relations'
	)
	
	person_role=models.ForeignKey(
		EnslavementRelationRole,
		null=False,
		blank=False,
		on_delete=models.CASCADE,
		related_name='person_relations'
	)
	
	person = models.ForeignKey(
		Person,
		null=False,
		blank=False,
		on_delete=models.CASCADE,
		related_name='person_relations'
	)
	document = models.ForeignKey(
		Documento,
		null=False,
		blank=False,
		on_delete=models.CASCADE,
		related_name='document_relations'
	)
	def __str__(self):
		return self.person.principal_alias + " " + self.document.resumen

