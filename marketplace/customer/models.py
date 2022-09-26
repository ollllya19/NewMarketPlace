from django.db import models
from api.models import Product
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="customer", null=True)
    phone = models.CharField(max_length=20, default="898723456")
    name = models.CharField(max_length=20)
    joined_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Cutomer"
        verbose_name_plural = "Customers"
        ordering = ["-id"]
        
    def __str__(self):
        return f"{self.name}"
    
    
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    deliv_date = models.DateField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
   
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ["-id"]
        
    def __str__(self):
        return f"{self.id}"
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    col = models.IntegerField(default=1)
    
    class Meta:
        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItems"
        ordering = ["-id"]
        
        unique_together = ('order', 'product')
        
    def __str__(self):
        return f"{self.id}"


class Cart(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_cart")
    col = models.IntegerField(default=1)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
        ordering = ["-id"]
        
        unique_together = ('product', 'user')
        
    def __str__(self):
        return f"{self.product.name}"
    

class Review(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    RATING = [(ONE, 1), (TWO, 2), (THREE, 3), (FOUR, 4), (FIVE, 5), ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField(default='')
    rating = models.IntegerField(
        choices=RATING,
        default=FIVE
    ) 
    created_at = models.DateTimeField(
          auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)
    