# Generated by Django 3.2.15 on 2022-08-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_auto_20220827_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default='name', max_length=20),
            preserve_default=False,
        ),
    ]
