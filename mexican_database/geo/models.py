from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator


class Polygon(models.Model):
	"""
	Shape of a spatial entity (optional for the locations that link to these)
	"""
	
	shape=models.JSONField(
		"Geojson Polygon",
		null=True,
		blank=True
	)

class LocationType(models.Model):
	"""
	Geographic Location Type
	We will default to points, but open up onto a polygons model for when we want to show countries etc
	"""

	name = models.CharField(
		"Geographic Location Type",
		max_length=255,
		unique=True
	)
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Geographic Location Type"
		verbose_name_plural = "Geographic Location Types"


class Location(models.Model):
	"""
	Geographic Location
	"""
	uuid=models.UUIDField(default=uuid.uuid4, editable=False,null=True)

	name = models.CharField(
		"Location name",
		max_length=255
	)
	longitude = models.DecimalField(
		"Longitude of Centroid",
		max_digits=10,
		decimal_places=7,
		null=True,
		blank=True
	)
	latitude = models.DecimalField(
		"Latitude of Centroid",
		max_digits=10,
		decimal_places=7,
		null=True,
		blank=True
	)
	
	parent = models.ForeignKey(
		'self',
		verbose_name="Child of",
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='children'
	)
	
	location_type = models.ForeignKey(
		'LocationType',
		verbose_name="Location Type",
		null=True,
		on_delete=models.SET_NULL,
		related_name='type_location'
	)
	
	spatial_extent = models.ForeignKey(
		'Polygon',
		verbose_name="Polygon",
		null=True,
		blank=True,
		on_delete=models.SET_NULL
	)
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Geographic Location"
		verbose_name_plural = "Geographic Locations"
