# Generated by Django 3.2.3 on 2021-10-21 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField(max_length=255)),
                ('category', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notification',
                'db_table': 'Notification',
            },
        ),
    ]