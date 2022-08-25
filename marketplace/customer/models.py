from django.db import models
from api.models import Product


class Customer(models.Model):
    phone = models.CharField(max_length=20, default="898723456", blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    date_joined=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    class Meta:
        verbose_name = "Cutomer"
        verbose_name_plural = "Customers"
        ordering = ["-id"]
        
    def __str__(self):
        return self.name
    
    
class Cart(models.Model):
    product_id=models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    amount=models.IntegerField()
    
    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
        ordering = ["-id"]
        
    def __str__(self):
        return self.product_id


class Order(models.Model):
    created_datetime=models.DateTimeField(auto_now_add=True)
    customer_id=models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer", blank=True, null=True)
    cart_id=models.OneToOneField(Cart, on_delete=models.CASCADE, related_name="cart", blank=True, null=True)
   
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ["-id"]
        
    def __str__(self):
        return self.created_datetime
    
    
    