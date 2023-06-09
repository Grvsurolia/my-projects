# Generated by Django 3.1.4 on 2021-10-19 08:21

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
            name='LeaveApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(blank=True, choices=[('casual leave', 'Casual Leave'), ('sick leave', 'Sick Leave'), ('comp off', 'Comp Off'), ('block leave', 'Block Leave'), ('maternity leave', 'Maternity Leave'), ('paternity leave', 'Paternity Leave'), ('bereavement leave', 'Bereavement Leave'), ('half-day', 'Half-Day'), ('other', 'Other')], max_length=50)),
                ('apply_date', models.DateField(auto_now_add=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('no_of_days', models.IntegerField(default=0)),
                ('reason', models.TextField()),
                ('to_time', models.TimeField(auto_now_add=True)),
                ('from_time', models.TimeField(auto_now_add=True)),
                ('onetime_hr_status', models.BooleanField(default=False)),
                ('overall_status', models.CharField(choices=[('approved', 'Approved'), ('pending', 'Pending'), ('reject', 'Reject')], default='pending', max_length=10)),
                ('total_leave', models.IntegerField(default=12)),
                ('remaining_leave', models.IntegerField(default=0)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Employees', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeLeave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_date', models.DateField(blank=True, null=True)),
                ('leave_type', models.CharField(choices=[('casual leave', 'Casual Leave'), ('sick leave', 'Sick Leave'), ('comp off', 'Comp Off'), ('block leave', 'Block Leave'), ('maternity leave', 'Maternity Leave'), ('paternity leave', 'Paternity Leave'), ('bereavement leave', 'Bereavement Leave'), ('half-day', 'Half-Day'), ('other', 'Other')], default='casual leave', max_length=255)),
                ('status', models.CharField(choices=[('approved', 'Approved'), ('pending', 'Pending'), ('reject', 'Reject')], default='pending', max_length=10)),
                ('employee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('leaves_apply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leave.leaveapplication')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeCancelLeave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_date', models.DateField(blank=True, null=True)),
                ('leave_type', models.CharField(choices=[('casual leave', 'Casual Leave'), ('sick leave', 'Sick Leave'), ('comp off', 'Comp Off'), ('block leave', 'Block Leave'), ('maternity leave', 'Maternity Leave'), ('paternity leave', 'Paternity Leave'), ('bereavement leave', 'Bereavement Leave'), ('half-day', 'Half-Day'), ('other', 'Other')], default='casual leave', max_length=255)),
                ('status', models.CharField(choices=[('approved', 'Approved'), ('pending', 'Pending'), ('reject', 'Reject')], default='reject', max_length=10)),
                ('employee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('leaves_apply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leave.leaveapplication')),
            ],
        ),
    ]
