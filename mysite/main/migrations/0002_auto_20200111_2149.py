# Generated by Django 2.2.5 on 2020-01-11 16:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_duration',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 21, 49, 25, 630115), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_stipend',
            field=models.IntegerField(default=0),
        ),
    ]
