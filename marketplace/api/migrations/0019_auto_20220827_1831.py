# Generated by Django 3.2.15 on 2022-08-27 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0018_alter_farmer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='name',
            field=models.CharField(blank=True, default='name', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='farmer',
            name='phone',
            field=models.CharField(blank=True, default='89872345672', max_length=20),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='farmer', to='auth.user'),
        ),
    ]
