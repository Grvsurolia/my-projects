# Generated by Django 3.1.4 on 2021-10-27 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_user_is_bde'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='status',
            field=models.CharField(choices=[('technical', 'Technical'), ('non-technical', 'Non-Technical'), ('management', 'Management'), ('other', 'Other')], default='technical', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='hr_common_email',
            field=models.EmailField(blank=True, default='hr@externlabs.com', max_length=254, null=True, verbose_name='Hr Email_address'),
        ),
    ]
