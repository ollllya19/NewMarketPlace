# Generated by Django 3.2.15 on 2022-09-19 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_auto_20220919_2146'),
        ('customer', '0021_auto_20220901_2205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='date_joined',
            new_name='joined_at',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='amount',
            new_name='col',
        ),
        migrations.AlterField(
            model_name='cart',
            name='col',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
            ],
        ),
    ]