from django.db import models
from api.models import Product


class Customer(models.Model):
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
    created_datetime = models.DateTimeField(auto_now_add=True)
    deliv_date = models.DateField()
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customer")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product")
    col = models.IntegerField()
   
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ["-id"]
        
    def __str__(self):
        return f"{self.created_datetime}"
    

"""
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Customer, on_delete=models.CASCADE)
    col = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItems"
        ordering = ["-id"]
        
    def __str__(self):
        return f"{self.id}"
"""



class Cart(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_cart")
    col = models.IntegerField(default=0)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customer_cart")
    
    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
        ordering = ["-id"]
        
    def __str__(self):
        return f"{self.product.title}"
    

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
    