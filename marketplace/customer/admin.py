from django.contrib import admin

from customer.models import Customer, Order, Cart, Review


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'name', 'joined_at')
    list_display_links = ('id', 'name')
    search_fields = ('phone', 'name')
    list_editable = ('phone',)
    list_filter = ('phone', 'name', 'joined_at')


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'col', 'user')
    list_display_links = ('id', 'product')
    search_fields = ('product',)
    list_editable = ('col',)
    list_filter = ('product', 'col', 'user')
    
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_datetime', 'deliv_date', 'customer', 'product', 'col')
    list_display_links = ('id',)
    search_fields = ('product', 'customer')
    list_filter = ('product', 'customer', 'deliv_date')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'text', 'rating', 'created_at', 'updated_at')
    list_display_links = ('id',)
    search_fields = ('product', 'customer', 'rating', 'created_at')
    list_filter = ('product', 'customer', 'rating')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Review, ReviewAdmin)
