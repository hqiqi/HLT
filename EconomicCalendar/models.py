from __future__ import unicode_literals

from django.db import models
import django_tables2 as tables

# Create your models here.
class EconomicReleases(models.Model):
	ID = models.AutoField(primary_key=True, null=False)
	EventID = models.CharField(max_length=60)
	Delay = models.CharField(max_length=60)
	EventCode = models.CharField(max_length=60)
	CountryCode = models.CharField(max_length=60)
	ReleasedOn = models.CharField(max_length=60)
	EventName = models.CharField(max_length=60)
	Values = models.CharField(max_length=500)
	Consensus = models.CharField(max_length=60)
	Actual = models.CharField(max_length=60)
	Message = models.CharField(max_length=60)
	Outcome = models.CharField(max_length=60)
	Identity = models.CharField(max_length=60)

	