# Generated by Django 3.0.3 on 2021-01-05 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('donor', '0001_initial'),
        ('fundraiser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donortransaction',
            name='fr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundraiser.Fundraiser'),
        ),
    ]
