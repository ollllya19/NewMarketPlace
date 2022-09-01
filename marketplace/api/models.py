from django.db import models
from django.contrib.auth.models import User


class Farmer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="farmer", null=True)
    phone = models.CharField(max_length=20, default="89872345672")
    name = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Farmer"
        verbose_name_plural = "Farmers"
        ordering = ["-id"]
        
    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    UOM = models.CharField(max_length=10, default="kg")
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-id"]
    
    def __str__(self):
        return f"{self.title}"
    
    
class Package(models.Model):
    ready_datetm = models.DateTimeField(auto_now_add=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name="farmer")
    order_id = models.BigIntegerField()
    is_accepted = models.BooleanField(default=False)
    is_packed = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Package"
        verbose_name_plural = "Packages"
        ordering = ["-id"]
    
    def __str__(self):
        return f"{self.order_id}"
    