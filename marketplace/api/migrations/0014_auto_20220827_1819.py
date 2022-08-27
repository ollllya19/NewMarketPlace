# Generated by Django 3.2.15 on 2022-08-27 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20220827_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='farmer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='farmer', to='api.farmer'),
        ),
        migrations.AlterField(
            model_name='package',
            name='order_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='package',
            name='ready_datetm',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]