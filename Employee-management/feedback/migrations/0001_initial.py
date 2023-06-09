# Generated by Django 3.1.4 on 2021-10-06 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_name', models.CharField(max_length=50)),
                ('incident_nature', models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative')], max_length=15)),
                ('priority', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('comments', models.TextField()),
                ('attach_file', models.FileField(blank=True, null=True, upload_to='file/')),
                ('incident_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='IncidentPerson', to=settings.AUTH_USER_MODEL)),
                ('responsible_person', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
