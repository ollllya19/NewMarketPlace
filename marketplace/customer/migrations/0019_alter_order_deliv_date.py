# Generated by Django 3.2.15 on 2022-09-01 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0018_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deliv_date',
            field=models.DateField(),
        ),
    ]
