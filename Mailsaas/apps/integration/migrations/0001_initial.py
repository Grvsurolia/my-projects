# Generated by Django 3.1.4 on 2021-03-09 09:00

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
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('team_id', models.CharField(max_length=20)),
                ('bot_user_id', models.CharField(max_length=20)),
                ('bot_access_token', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SalesForceDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(blank=True, max_length=200)),
                ('object_type_people', models.CharField(choices=[('Leads', 'Lead'), ('Contacts', 'Contact')], default='Contacts', max_length=12)),
                ('missing', models.CharField(choices=[('Create them', 'Create them'), ('Do nothing', 'Do nothing')], default='Contacts', max_length=20)),
                ('track_event', models.CharField(choices=[('All Mailsaas Prospects', 'All Mailsaas Prospects'), ('Only Mailsaas Leads', 'Only Mailsaas Leads')], default='Contacts', max_length=50)),
                ('sends', models.BooleanField(default=True)),
                ('opens', models.BooleanField(default=True)),
                ('clicks', models.BooleanField(default=True)),
                ('replies', models.BooleanField(default=True)),
                ('unsubscribed', models.BooleanField(default=True)),
                ('leads', models.BooleanField(default=True)),
                ('tasks', models.BooleanField(default=True)),
                ('phone_calls', models.BooleanField(default=False)),
                ('lead_opened', models.CharField(choices=[('none', 'None'), ('Open-Not Contacted', 'Open-Not Contacted'), ('Working-Contacted', 'Working-Contacted'), ('Closed-Converted', 'Closed-Converted'), ('Closed-Not Converted', 'Closed-Not Converted')], default='none', max_length=90)),
                ('lead_ignored', models.CharField(choices=[('none', 'None'), ('Open-Not Contacted', 'Open-Not Contacted'), ('Working-Contacted', 'Working-Contacted'), ('Closed-Converted', 'Closed-Converted'), ('Closed-Not Converted', 'Closed-Not Converted')], default='none', max_length=90)),
                ('lead_won', models.CharField(choices=[('none', 'None'), ('Open-Not Contacted', 'Open-Not Contacted'), ('Working-Contacted', 'Working-Contacted'), ('Closed-Converted', 'Closed-Converted'), ('Closed-Not Converted', 'Closed-Not Converted')], default='none', max_length=90)),
                ('lead_lost', models.CharField(choices=[('none', 'None'), ('Open-Not Contacted', 'Open-Not Contacted'), ('Working-Contacted', 'Working-Contacted'), ('Closed-Converted', 'Closed-Converted'), ('Closed-Not Converted', 'Closed-Not Converted')], default='none', max_length=90)),
                ('lead_unsubcribed', models.CharField(choices=[('none', 'None'), ('Open-Not Contacted', 'Open-Not Contacted'), ('Working-Contacted', 'Working-Contacted'), ('Closed-Converted', 'Closed-Converted'), ('Closed-Not Converted', 'Closed-Not Converted')], default='none', max_length=90)),
                ('lead_resubscribed', models.CharField(choices=[('none', 'None'), ('Open-Not Contacted', 'Open-Not Contacted'), ('Working-Contacted', 'Working-Contacted'), ('Closed-Converted', 'Closed-Converted'), ('Closed-Not Converted', 'Closed-Not Converted')], default='none', max_length=90)),
                ('email_bounced', models.CharField(choices=[('none', 'None'), ('Open-Not Contacted', 'Open-Not Contacted'), ('Working-Contacted', 'Working-Contacted'), ('Closed-Converted', 'Closed-Converted'), ('Closed-Not Converted', 'Closed-Not Converted')], default='none', max_length=90)),
                ('is_delete', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
