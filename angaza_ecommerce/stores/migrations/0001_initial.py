# Generated by Django 3.2.3 on 2021-10-21 11:17

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('the_json', jsonfield.fields.JSONField(default=dict)),
            ],
            options={
                'verbose_name': 'ProductSpecification',
                'verbose_name_plural': 'ProductSpecification',
                'db_table': 'ProductSpecification',
            },
        ),
        migrations.CreateModel(
            name='StoreOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.store')),
            ],
            options={
                'verbose_name': 'StoreOwner',
                'verbose_name_plural': 'StoreOwner',
                'db_table': 'StoreOwner',
            },
        ),
    ]