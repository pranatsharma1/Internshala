# Generated by Django 2.2.5 on 2019-09-23 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20190923_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 23, 22, 40, 25, 858304), verbose_name='date published'),
        ),
    ]