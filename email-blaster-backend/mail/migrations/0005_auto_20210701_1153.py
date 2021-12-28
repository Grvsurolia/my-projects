# Generated by Django 3.1.7 on 2021-07-01 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0004_auto_20210413_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailsentstatus',
            name='is_linked_clicked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mailsentstatus',
            name='link_count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
