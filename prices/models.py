from __future__ import unicode_literals

from django.db import models

# Create your models here.
class price_m1(models.Model):
   DateTime = models.CharField(primary_key=True,verbose_name="dt", max_length=60)
   Date = models.CharField(verbose_name="d", max_length=60)
   Time = models.CharField(verbose_name="t", max_length=60)
   c1 = models.DecimalField(verbose_name="c1", max_digits=15, decimal_places=10,null=True)
   c2 = models.DecimalField(verbose_name="c2", max_digits=15, decimal_places=10,null=True)
   c3 = models.DecimalField(verbose_name="c3", max_digits=15, decimal_places=10,null=True)
   c4 = models.DecimalField(verbose_name="c4", max_digits=15, decimal_places=10,null=True)
   c5 = models.DecimalField(verbose_name="c5", max_digits=15, decimal_places=10,null=True)
   c6 = models.DecimalField(verbose_name="c6", max_digits=15, decimal_places=10,null=True)
   c7 = models.DecimalField(verbose_name="c7", max_digits=15, decimal_places=10,null=True)
   c8 = models.DecimalField(verbose_name="c8", max_digits=15, decimal_places=10,null=True)
   c9 = models.DecimalField(verbose_name="c9", max_digits=15, decimal_places=10,null=True)
   c10 = models.DecimalField(verbose_name="c10", max_digits=15, decimal_places=10,null=True)
   c11 = models.DecimalField(verbose_name="c11", max_digits=15, decimal_places=10,null=True)
   c12 = models.DecimalField(verbose_name="c12", max_digits=15, decimal_places=10,null=True)
   c13 = models.DecimalField(verbose_name="c13", max_digits=15, decimal_places=10,null=True)
   c14 = models.DecimalField(verbose_name="c14", max_digits=15, decimal_places=10,null=True)
   c15 = models.DecimalField(verbose_name="c15", max_digits=15, decimal_places=10,null=True)
   c16 = models.DecimalField(verbose_name="c16", max_digits=15, decimal_places=10,null=True)
   c17 = models.DecimalField(verbose_name="c17", max_digits=15, decimal_places=10,null=True)
   c18 = models.DecimalField(verbose_name="c18", max_digits=15, decimal_places=10,null=True)
   c19 = models.DecimalField(verbose_name="c19", max_digits=15, decimal_places=10,null=True)
   c20 = models.DecimalField(verbose_name="c20", max_digits=15, decimal_places=10,null=True)
   c21 = models.DecimalField(verbose_name="c21", max_digits=15, decimal_places=10,null=True)
   c22 = models.DecimalField(verbose_name="c22", max_digits=15, decimal_places=10,null=True)
   c23 = models.DecimalField(verbose_name="c23", max_digits=15, decimal_places=10,null=True)
   c24 = models.DecimalField(verbose_name="c24", max_digits=15, decimal_places=10,null=True)
   c25 = models.DecimalField(verbose_name="c25", max_digits=15, decimal_places=10,null=True)
   c26 = models.DecimalField(verbose_name="c26", max_digits=15, decimal_places=10,null=True)
   c27 = models.DecimalField(verbose_name="c27", max_digits=15, decimal_places=10,null=True)
   c28 = models.DecimalField(verbose_name="c28", max_digits=15, decimal_places=10,null=True)

class price_m5(models.Model):
   DateTime = models.CharField(primary_key=True,verbose_name="dt", max_length=60)
   Date = models.CharField(verbose_name="d", max_length=60)
   Time = models.CharField(verbose_name="t", max_length=60)
   c1 = models.DecimalField(verbose_name="c1", max_digits=15, decimal_places=10)
   c2 = models.DecimalField(verbose_name="c2", max_digits=15, decimal_places=10)
   c3 = models.DecimalField(verbose_name="c3", max_digits=15, decimal_places=10)
   c4 = models.DecimalField(verbose_name="c4", max_digits=15, decimal_places=10)
   c5 = models.DecimalField(verbose_name="c5", max_digits=15, decimal_places=10)
   c6 = models.DecimalField(verbose_name="c6", max_digits=15, decimal_places=10)
   c7 = models.DecimalField(verbose_name="c7", max_digits=15, decimal_places=10)
   c8 = models.DecimalField(verbose_name="c8", max_digits=15, decimal_places=10,null=True)
   c9 = models.DecimalField(verbose_name="c9", max_digits=15, decimal_places=10,null=True)
   c10 = models.DecimalField(verbose_name="c10", max_digits=15, decimal_places=10,null=True)
   c11 = models.DecimalField(verbose_name="c11", max_digits=15, decimal_places=10,null=True)
   c12 = models.DecimalField(verbose_name="c12", max_digits=15, decimal_places=10,null=True)
   c13 = models.DecimalField(verbose_name="c13", max_digits=15, decimal_places=10,null=True)
   c14 = models.DecimalField(verbose_name="c14", max_digits=15, decimal_places=10,null=True)
   c15 = models.DecimalField(verbose_name="c15", max_digits=15, decimal_places=10,null=True)
   c16 = models.DecimalField(verbose_name="c16", max_digits=15, decimal_places=10,null=True)
   c17 = models.DecimalField(verbose_name="c17", max_digits=15, decimal_places=10,null=True)
   c18 = models.DecimalField(verbose_name="c18", max_digits=15, decimal_places=10,null=True)
   c19 = models.DecimalField(verbose_name="c19", max_digits=15, decimal_places=10,null=True)
   c20 = models.DecimalField(verbose_name="c20", max_digits=15, decimal_places=10,null=True)
   c21 = models.DecimalField(verbose_name="c21", max_digits=15, decimal_places=10,null=True)
   c22 = models.DecimalField(verbose_name="c22", max_digits=15, decimal_places=10,null=True)
   c23 = models.DecimalField(verbose_name="c23", max_digits=15, decimal_places=10,null=True)
   c24 = models.DecimalField(verbose_name="c24", max_digits=15, decimal_places=10,null=True)
   c25 = models.DecimalField(verbose_name="c25", max_digits=15, decimal_places=10,null=True)
   c26 = models.DecimalField(verbose_name="c26", max_digits=15, decimal_places=10,null=True)
   c27 = models.DecimalField(verbose_name="c27", max_digits=15, decimal_places=10,null=True)
   c28 = models.DecimalField(verbose_name="c28", max_digits=15, decimal_places=10,null=True)
   

class price_m15(models.Model):
   DateTime = models.CharField(primary_key=True,verbose_name="dt", max_length=60)
   Date = models.CharField(verbose_name="d", max_length=60)
   Time = models.CharField(verbose_name="t", max_length=60)
   c1 = models.DecimalField(verbose_name="c1", max_digits=15, decimal_places=10)
   c2 = models.DecimalField(verbose_name="c2", max_digits=15, decimal_places=10)
   c3 = models.DecimalField(verbose_name="c3", max_digits=15, decimal_places=10)
   c4 = models.DecimalField(verbose_name="c4", max_digits=15, decimal_places=10)
   c5 = models.DecimalField(verbose_name="c5", max_digits=15, decimal_places=10)
   c6 = models.DecimalField(verbose_name="c6", max_digits=15, decimal_places=10)
   c7 = models.DecimalField(verbose_name="c7", max_digits=15, decimal_places=10)
   c8 = models.DecimalField(verbose_name="c8", max_digits=15, decimal_places=10,null=True)
   c9 = models.DecimalField(verbose_name="c9", max_digits=15, decimal_places=10,null=True)
   c10 = models.DecimalField(verbose_name="c10", max_digits=15, decimal_places=10,null=True)
   c11 = models.DecimalField(verbose_name="c11", max_digits=15, decimal_places=10,null=True)
   c12 = models.DecimalField(verbose_name="c12", max_digits=15, decimal_places=10,null=True)
   c13 = models.DecimalField(verbose_name="c13", max_digits=15, decimal_places=10,null=True)
   c14 = models.DecimalField(verbose_name="c14", max_digits=15, decimal_places=10,null=True)
   c15 = models.DecimalField(verbose_name="c15", max_digits=15, decimal_places=10,null=True)
   c16 = models.DecimalField(verbose_name="c16", max_digits=15, decimal_places=10,null=True)
   c17 = models.DecimalField(verbose_name="c17", max_digits=15, decimal_places=10,null=True)
   c18 = models.DecimalField(verbose_name="c18", max_digits=15, decimal_places=10,null=True)
   c19 = models.DecimalField(verbose_name="c19", max_digits=15, decimal_places=10,null=True)
   c20 = models.DecimalField(verbose_name="c20", max_digits=15, decimal_places=10,null=True)
   c21 = models.DecimalField(verbose_name="c21", max_digits=15, decimal_places=10,null=True)
   c22 = models.DecimalField(verbose_name="c22", max_digits=15, decimal_places=10,null=True)
   c23 = models.DecimalField(verbose_name="c23", max_digits=15, decimal_places=10,null=True)
   c24 = models.DecimalField(verbose_name="c24", max_digits=15, decimal_places=10,null=True)
   c25 = models.DecimalField(verbose_name="c25", max_digits=15, decimal_places=10,null=True)
   c26 = models.DecimalField(verbose_name="c26", max_digits=15, decimal_places=10,null=True)
   c27 = models.DecimalField(verbose_name="c27", max_digits=15, decimal_places=10,null=True)
   c28 = models.DecimalField(verbose_name="c28", max_digits=15, decimal_places=10,null=True)
   
class price_m30(models.Model):
   DateTime = models.CharField(primary_key=True,verbose_name="dt", max_length=60)
   Date = models.CharField(verbose_name="d", max_length=60)
   Time = models.CharField(verbose_name="t", max_length=60)
   c1 = models.DecimalField(verbose_name="c1", max_digits=15, decimal_places=10)
   c2 = models.DecimalField(verbose_name="c2", max_digits=15, decimal_places=10)
   c3 = models.DecimalField(verbose_name="c3", max_digits=15, decimal_places=10)
   c4 = models.DecimalField(verbose_name="c4", max_digits=15, decimal_places=10)
   c5 = models.DecimalField(verbose_name="c5", max_digits=15, decimal_places=10)
   c6 = models.DecimalField(verbose_name="c6", max_digits=15, decimal_places=10)
   c7 = models.DecimalField(verbose_name="c7", max_digits=15, decimal_places=10)
   c8 = models.DecimalField(verbose_name="c8", max_digits=15, decimal_places=10,null=True)
   c9 = models.DecimalField(verbose_name="c9", max_digits=15, decimal_places=10,null=True)
   c10 = models.DecimalField(verbose_name="c10", max_digits=15, decimal_places=10,null=True)
   c11 = models.DecimalField(verbose_name="c11", max_digits=15, decimal_places=10,null=True)
   c12 = models.DecimalField(verbose_name="c12", max_digits=15, decimal_places=10,null=True)
   c13 = models.DecimalField(verbose_name="c13", max_digits=15, decimal_places=10,null=True)
   c14 = models.DecimalField(verbose_name="c14", max_digits=15, decimal_places=10,null=True)
   c15 = models.DecimalField(verbose_name="c15", max_digits=15, decimal_places=10,null=True)
   c16 = models.DecimalField(verbose_name="c16", max_digits=15, decimal_places=10,null=True)
   c17 = models.DecimalField(verbose_name="c17", max_digits=15, decimal_places=10,null=True)
   c18 = models.DecimalField(verbose_name="c18", max_digits=15, decimal_places=10,null=True)
   c19 = models.DecimalField(verbose_name="c19", max_digits=15, decimal_places=10,null=True)
   c20 = models.DecimalField(verbose_name="c20", max_digits=15, decimal_places=10,null=True)
   c21 = models.DecimalField(verbose_name="c21", max_digits=15, decimal_places=10,null=True)
   c22 = models.DecimalField(verbose_name="c22", max_digits=15, decimal_places=10,null=True)
   c23 = models.DecimalField(verbose_name="c23", max_digits=15, decimal_places=10,null=True)
   c24 = models.DecimalField(verbose_name="c24", max_digits=15, decimal_places=10,null=True)
   c25 = models.DecimalField(verbose_name="c25", max_digits=15, decimal_places=10,null=True)
   c26 = models.DecimalField(verbose_name="c26", max_digits=15, decimal_places=10,null=True)
   c27 = models.DecimalField(verbose_name="c27", max_digits=15, decimal_places=10,null=True)
   c28 = models.DecimalField(verbose_name="c28", max_digits=15, decimal_places=10,null=True)
   

class price_H1(models.Model):
   DateTime = models.CharField(primary_key=True,verbose_name="dt", max_length=60)
   Date = models.CharField(verbose_name="d", max_length=60)
   Time = models.CharField(verbose_name="t", max_length=60)
   c1 = models.DecimalField(verbose_name="c1", max_digits=15, decimal_places=10)
   c2 = models.DecimalField(verbose_name="c2", max_digits=15, decimal_places=10)
   c3 = models.DecimalField(verbose_name="c3", max_digits=15, decimal_places=10)
   c4 = models.DecimalField(verbose_name="c4", max_digits=15, decimal_places=10)
   c5 = models.DecimalField(verbose_name="c5", max_digits=15, decimal_places=10)
   c6 = models.DecimalField(verbose_name="c6", max_digits=15, decimal_places=10)
   c7 = models.DecimalField(verbose_name="c7", max_digits=15, decimal_places=10)
   c8 = models.DecimalField(verbose_name="c8", max_digits=15, decimal_places=10,null=True)
   c9 = models.DecimalField(verbose_name="c9", max_digits=15, decimal_places=10,null=True)
   c10 = models.DecimalField(verbose_name="c10", max_digits=15, decimal_places=10,null=True)
   c11 = models.DecimalField(verbose_name="c11", max_digits=15, decimal_places=10,null=True)
   c12 = models.DecimalField(verbose_name="c12", max_digits=15, decimal_places=10,null=True)
   c13 = models.DecimalField(verbose_name="c13", max_digits=15, decimal_places=10,null=True)
   c14 = models.DecimalField(verbose_name="c14", max_digits=15, decimal_places=10,null=True)
   c15 = models.DecimalField(verbose_name="c15", max_digits=15, decimal_places=10,null=True)
   c16 = models.DecimalField(verbose_name="c16", max_digits=15, decimal_places=10,null=True)
   c17 = models.DecimalField(verbose_name="c17", max_digits=15, decimal_places=10,null=True)
   c18 = models.DecimalField(verbose_name="c18", max_digits=15, decimal_places=10,null=True)
   c19 = models.DecimalField(verbose_name="c19", max_digits=15, decimal_places=10,null=True)
   c20 = models.DecimalField(verbose_name="c20", max_digits=15, decimal_places=10,null=True)
   c21 = models.DecimalField(verbose_name="c21", max_digits=15, decimal_places=10,null=True)
   c22 = models.DecimalField(verbose_name="c22", max_digits=15, decimal_places=10,null=True)
   c23 = models.DecimalField(verbose_name="c23", max_digits=15, decimal_places=10,null=True)
   c24 = models.DecimalField(verbose_name="c24", max_digits=15, decimal_places=10,null=True)
   c25 = models.DecimalField(verbose_name="c25", max_digits=15, decimal_places=10,null=True)
   c26 = models.DecimalField(verbose_name="c26", max_digits=15, decimal_places=10,null=True)
   c27 = models.DecimalField(verbose_name="c27", max_digits=15, decimal_places=10,null=True)
   c28 = models.DecimalField(verbose_name="c28", max_digits=15, decimal_places=10,null=True)
