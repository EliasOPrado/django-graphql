from django.db import models

# Create your models here.
class ProductModel(models.Model):
    Segment = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Product = models.CharField(max_length=100)
    Units = models.IntegerField(max_length=100)
    Sales = models.IntegerField(max_length=100)
    DateSold = models.CharField(max_length=100)

    def __str__(self):
        return self.product