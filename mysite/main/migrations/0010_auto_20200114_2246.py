# Generated by Django 2.2.5 on 2020-01-14 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200114_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 14, 22, 46, 45, 148729), verbose_name='date published'),
        ),
    ]