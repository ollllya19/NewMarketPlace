# Generated by Django 3.2.15 on 2022-08-16 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220816_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='phone',
            field=models.CharField(default='89872345672', max_length=20),
        ),
    ]