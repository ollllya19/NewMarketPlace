# Generated by Django 3.2.15 on 2022-08-05 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Farmer',
                'verbose_name_plural': 'Farmers',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=500)),
                ('farmer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.farmer')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-id'],
            },
        ),
    ]
