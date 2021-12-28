# Generated by Django 3.2.3 on 2021-10-21 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_price', models.FloatField()),
                ('MRP_price', models.FloatField()),
                ('total_price', models.FloatField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookingForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.FloatField(blank=True, default=0.0, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=13, null=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('apartment', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Booking Form',
                'verbose_name_plural': 'Booking Form',
                'db_table': 'Booking Form',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_date', models.DateField(auto_now_add=True)),
                ('delivered_date', models.DateField(auto_now_add=True, null=True)),
                ('being_delivered', models.BooleanField(default=False)),
                ('order_cancel', models.BooleanField(default=False)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('buy', models.BooleanField(default=False)),
                ('booking', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Order',
                'db_table': 'Order',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('status', models.CharField(blank=True, choices=[('Declain', 'Declain'), ('Accept', 'Accept')], max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Order Product',
                'verbose_name_plural': 'Order Product',
                'db_table': 'Order Product',
            },
        ),
        migrations.CreateModel(
            name='SubBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_price', models.FloatField()),
                ('MRP_price', models.FloatField()),
                ('total_price', models.FloatField()),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Bill',
                'verbose_name_plural': 'Bill',
                'db_table': 'Bill',
            },
        ),
    ]
