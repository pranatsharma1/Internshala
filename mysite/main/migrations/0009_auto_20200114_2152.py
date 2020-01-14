# Generated by Django 2.2.5 on 2020-01-14 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200114_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='intern',
            name='email',
            field=models.EmailField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 14, 21, 52, 11, 139752), verbose_name='date published'),
        ),
    ]