from time import timezone
from django.db import models
from api.models import Product


class Customer(models.Model):
    phone = models.CharField(max_length=20, default="898723456")
    name = models.CharField(max_length=20)
    date_joined=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Cutomer"
        verbose_name_plural = "Customers"
        ordering = ["-id"]
        
    def __str__(self):
        return f"{self.name}"
    
    
class Order(models.Model):
    created_datetime=models.DateTimeField(auto_now_add=True)
    deliv_date=models.DateField(auto_now_add=True)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer", null=True)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product", null=True)
    amount=models.IntegerField()
   
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ["-id"]
        
    def __str__(self):
        return f"{self.created_datetime}"