from django.db import models


class Farmer(models.Model):
    mail = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20, default="89872345672")
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100, blank=True)
    
    class Meta:
        verbose_name = "Farmer"
        verbose_name_plural = "Farmers"
        ordering = ["-id"]
        
    def __str__(self):
        return f'{self.id}: {self.name}'


class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-id"]
    
    def __str__(self):
        return f'{self.id}: {self.title}'
    