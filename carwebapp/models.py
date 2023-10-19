from django.db import models
from carapp.models import Carproductdb

# Create your models here.

class registerdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    CPassword = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(null=True, blank=True)

class Checkoutdb(models.Model):
    Carname = models.CharField(max_length=100, null=True, blank=True)
    Yearman = models.IntegerField(null=True, blank=True)
    Prokms = models.IntegerField(null=True, blank=True)
    Profuel = models.CharField(max_length=100, null=True, blank=True)
    Pricecar = models.IntegerField(null=True, blank=True)
    Register = models.ForeignKey(registerdb, on_delete=models.CASCADE, null=True)

class contactdb(models.Model):
    Yname = models.CharField(max_length=100, null=True, blank=True)
    Yemail = models.EmailField(max_length=100, null=True, blank=True)
    Subjct = models.CharField(max_length=100, null=True, blank=True)
    Messeges = models.CharField(max_length=100, null=True, blank=True)

class SearchResults(models.Model):
    query = models.CharField(max_length=100)
    product = models.ForeignKey(Carproductdb, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.query} - {self.product.ProName3}"

class Carselldb(models.Model):
    CataName7 = models.CharField(max_length=100, null=True, blank=True)
    ProName7 = models.CharField(max_length=100, null=True, blank=True)
    Proyear7 = models.IntegerField(null=True, blank=True)
    Prokms7 = models.IntegerField(null=True, blank=True)
    Profuel7 = models.CharField(max_length=100, null=True, blank=True)
    ProPrice7 = models.IntegerField(null=True, blank=True)
    ProDescription7 = models.CharField(max_length=500, null=True, blank=True)
    ProImage7 = models.ImageField(upload_to="product_photo", null=True, blank=True)
    Yrmob = models.IntegerField(null=True, blank=True)
    Yname2 = models.CharField(max_length=100, null=True, blank=True)
    Yemail2 = models.EmailField(max_length=100, null=True, blank=True)


