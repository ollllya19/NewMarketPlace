# Generated by Django 3.2.15 on 2022-08-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deliv_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
