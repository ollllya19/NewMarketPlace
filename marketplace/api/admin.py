from django.contrib import admin

from api.models import Farmer, Product, Package


class FarmerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone', 'address', 'joined_date')
    list_display_links = ('id', 'user')
    search_fields = ('phone', 'user', 'joined_date')
    list_editable = ('address',)
    list_filter = ('user', 'name', 'joined_date')


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'description', 'price', 'UOM', 'user', 'created_at', 'updated_at')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'price', 'user')
    list_filter = ('name', 'price', 'user')


admin.site.register(Farmer, FarmerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Package)
