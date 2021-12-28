# Generated by Django 3.1.4 on 2021-01-06 08:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestedUpdateFundraiser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=50)),
                ('cause', models.CharField(choices=[('medical', 'MEDICAL')], max_length=20)),
                ('beneficiaryFullName', models.CharField(max_length=50)),
                ('beneficiaryAge', models.PositiveIntegerField()),
                ('beneficiaryGender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('cityOfResidence', models.CharField(max_length=100)),
                ('goalAmount', models.FloatField(validators=[django.core.validators.MinValueValidator(200)])),
                ('is_active', models.BooleanField(default=False)),
                ('story', models.TextField(max_length=1000)),
                ('isPrivate', models.BooleanField(default=False)),
                ('beneficiaryPhoto', models.ImageField(upload_to='patientImg')),
                ('lastDateToFund', models.CharField(max_length=100)),
                ('beneficiaryDocument', models.FileField(upload_to='documentImg')),
                ('created_date_time', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
