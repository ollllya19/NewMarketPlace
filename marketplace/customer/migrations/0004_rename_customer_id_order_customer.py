# Generated by Django 3.2.15 on 2022-08-27 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20220827_0017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer_id',
            new_name='customer',
        ),
    ]
