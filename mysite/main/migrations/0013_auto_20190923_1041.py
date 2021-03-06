# Generated by Django 2.2.5 on 2019-09-23 05:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20190922_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intern',
            name='id_job',
        ),
        migrations.RemoveField(
            model_name='job',
            name='id_job',
        ),
        migrations.AddField(
            model_name='intern',
            name='company_name',
            field=models.CharField(default='Samsung', max_length=100),
        ),
        migrations.AddField(
            model_name='intern',
            name='job_id',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 23, 10, 41, 49, 15213), verbose_name='date published'),
        ),
    ]
