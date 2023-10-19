from django.db import models

# Create your models here.
class Catacarsdb(models.Model):
    Name3 = models.CharField(max_length=100, null=True, blank=True)
    Description3 = models.CharField(max_length=500, null=True, blank=True)
    Image6 = models.ImageField(upload_to="product_photo", null=True, blank=True)


class Carproductdb(models.Model):
    CataName3 = models.CharField(max_length=100, null=True, blank=True)
    ProName3 = models.CharField(max_length=100, null=True, blank=True)
    Proyear = models.IntegerField(null=True, blank=True)
    Prokms = models.IntegerField(null=True, blank=True)
    Profuel = models.CharField(max_length=100, null=True, blank=True)
    ProPrice = models.IntegerField(null=True, blank=True)
    ProDescription3 = models.CharField(max_length=500, null=True, blank=True)
    ProImage6 = models.ImageField(upload_to="product_photo", null=True, blank=True)


class ratingdb(models.Model):
    Yr_name = models.CharField(max_length=100, null=True, blank=True)
    Email8 = models.EmailField(max_length=100, null=True, blank=True)
    Yr_rating = models.CharField(max_length=500, null=True, blank=True)
    Yr_photo = models.ImageField(upload_to="Client_photo", null=True, blank=True)