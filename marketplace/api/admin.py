from atexit import register
from django.contrib import admin

from api.models import Farmer, Product


admin.site.register(Farmer)
admin.site.register(Product)