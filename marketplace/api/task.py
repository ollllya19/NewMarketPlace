from __future__ import absolute_import, unicode_literals
from marketplace.celery import app

from customer.models import Order
from api.models import Package


@app.task()
def create_package_from_order(order_id):
    order = Order.objects.get(id=order_id)
    farmer = order.product.farmer
    package = Package.objects.create(farmer=farmer, order_id=order_id)
    package.save()
