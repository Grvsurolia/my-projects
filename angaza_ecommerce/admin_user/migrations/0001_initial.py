# Generated by Django 3.2.3 on 2021-10-21 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Admin User',
                'verbose_name_plural': 'Admin User',
                'db_table': 'Admin User',
            },
        ),
        migrations.CreateModel(
            name='DetailPagesAdvertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='Advertisement/')),
                ('url', models.URLField(default='https://www.dealzmoto.com/', max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Detail Page Advertisement',
                'verbose_name_plural': 'Detail Page Advertisement',
            },
        ),
        migrations.CreateModel(
            name='HomePagesAdvertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_number', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)])),
                ('thumbnail', models.ImageField(upload_to='Advertisement/')),
                ('url', models.URLField(default='https://www.dealzmoto.com/', max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Home Page Advertisement',
                'verbose_name_plural': 'Home Page Advertisement',
                'db_table': 'Home Page Advertisement',
            },
        ),
    ]