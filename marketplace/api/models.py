from django.db import models
from django.contrib.auth.models import User


class Farmer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="farmer", blank=True, null=True)
    phone = models.CharField(max_length=20, default="89872345672", blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    date_joined=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    class Meta:
        verbose_name = "Farmer"
        verbose_name_plural = "Farmers"
        ordering = ["-id"]
        
    def __str__(self):
        return self.user.username


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
    