# Generated by Django 3.2.15 on 2022-08-27 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0017_alter_package_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='farmer', to=settings.AUTH_USER_MODEL),
        ),
    ]