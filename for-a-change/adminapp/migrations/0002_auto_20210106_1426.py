# Generated by Django 3.1.4 on 2021-01-06 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fundraiser', '0004_auto_20210106_1400'),
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestedupdatefundraiser',
            name='frTitle',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requestedupdatefundraiser',
            name='frid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fundraiser.fundraiser'),
            preserve_default=False,
        ),
    ]
