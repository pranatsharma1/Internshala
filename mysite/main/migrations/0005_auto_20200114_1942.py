# Generated by Django 2.2.5 on 2020-01-14 14:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200112_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 14, 19, 42, 3, 232393), verbose_name='date published'),
        ),
    ]
