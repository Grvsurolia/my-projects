# Generated by Django 3.1.4 on 2021-01-05 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0002_donortransaction_fr'),
    ]

    operations = [
        migrations.AddField(
            model_name='donortransaction',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]