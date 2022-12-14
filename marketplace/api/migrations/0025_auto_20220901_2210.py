# Generated by Django 3.2.15 on 2022-09-01 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20220827_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='UOM',
            field=models.CharField(default='kg', max_length=10),
        ),
        migrations.AlterField(
            model_name='package',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farmer', to='api.farmer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.farmer'),
        ),
    ]
