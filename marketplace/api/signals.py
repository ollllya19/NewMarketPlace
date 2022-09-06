from django.db.models.signals import post_save
from django.dispatch import receiver

from customer.models import Order
from api.task import create_package_from_order


@receiver(post_save, sender=Order)
def send_email(sender, instance, created, **kwargs):
    create_package_from_order.delay(instance.id)
    