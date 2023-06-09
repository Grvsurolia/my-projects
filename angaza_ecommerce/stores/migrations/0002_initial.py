# Generated by Django 3.2.3 on 2021-10-21 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeowner',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productspecification',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
