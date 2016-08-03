from __future__ import unicode_literals

from django.db import models
import django_tables2 as tables

class USD_MADdash(models.Model):
	ID = models.AutoField(primary_key=True, null=False)
	USD = models.CharField(unique=True, max_length=60)
	M1 = models.IntegerField()
	M5 = models.IntegerField()
	M15 = models.IntegerField()
	M30 = models.IntegerField()
	H1 = models.IntegerField()

class EUR_MADdash(models.Model):
	ID = models.AutoField(primary_key=True, null=False)
	EUR = models.CharField(unique=True, max_length=60)
	M1 = models.IntegerField()
	M5 = models.IntegerField()
	M15 = models.IntegerField()
	M30 = models.IntegerField()
	H1 = models.IntegerField()

class GBP_MADdash(models.Model):
	ID = models.AutoField(primary_key=True, null=False)
	GBP = models.CharField(unique=True, max_length=60)
	M1 = models.IntegerField()
	M5 = models.IntegerField()
	M15 = models.IntegerField()
	M30 = models.IntegerField()
	H1 = models.IntegerField()

class JPY_MADdash(models.Model):
	ID = models.AutoField(primary_key=True, null=False)
	JPY = models.CharField(unique=True, max_length=60)
	M1 = models.IntegerField()
	M5 = models.IntegerField()
	M15 = models.IntegerField()
	M30 = models.IntegerField()
	H1 = models.IntegerField()

class AUD_MADdash(models.Model):
	ID = models.AutoField(primary_key=True, null=False)
	AUD = models.CharField(unique=True, max_length=60)
	M1 = models.IntegerField()
	M5 = models.IntegerField()
	M15 = models.IntegerField()
	M30 = models.IntegerField()
	H1 = models.IntegerField()

class NZD_MADdash(models.Model):
	ID = models.AutoField(primary_key=True, null=False)
	NZD = models.CharField(unique=True, max_length=60)
	M1 = models.IntegerField()
	M5 = models.IntegerField()
	M15 = models.IntegerField()
	M30 = models.IntegerField()
	H1 = models.IntegerField()

class CHF_MADdash(models.Model):
	ID = models.AutoField(primary_key=True, null=False)
	CHF = models.CharField(unique=True,max_length=60)
	M1 = models.IntegerField()
	M5 = models.IntegerField()
	M15 = models.IntegerField()
	M30 = models.IntegerField()
	H1 = models.IntegerField()

class CAD_MADdash(models.Model):
	ID = models.AutoField(primary_key=True, null=False)
	CAD = models.CharField(unique=True, max_length=60)
	M1 = models.IntegerField()
	M5 = models.IntegerField()
	M15 = models.IntegerField()
	M30 = models.IntegerField()
	H1 = models.IntegerField()


