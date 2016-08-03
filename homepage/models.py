from __future__ import unicode_literals

from django.db import models
import django_tables2 as tables
# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=False,null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.email

class EconomicRelease(models.Model):
    Time = models.CharField(verbose_name="Time", max_length=60)
    Currency = models.CharField(verbose_name="Currency", max_length=60)
    Impact = models.CharField(verbose_name="Impact", max_length=60)
    Detail = models.CharField(verbose_name="Detail", max_length=60)
    Actual = models.CharField(verbose_name="Actual", max_length=60)
    Forecast = models.CharField(verbose_name="Forecast", max_length=60)
    Previous = models.CharField(verbose_name="Previous", max_length=60)

class MADdash(models.Model):
    USD = models.CharField(verbose_name="USD", max_length=60)
    M1 = models.CharField(verbose_name="M1", max_length=60)
    M5 = models.CharField(verbose_name="M5", max_length=60)
    M15 = models.CharField(verbose_name="M15", max_length=60)
    M30 = models.CharField(verbose_name="M30", max_length=60)
    H1 = models.CharField(verbose_name="H1", max_length=60)
  
