from atexit import register
from django.contrib import admin

from customer.models import Customer, Order, Cart


admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Cart)
