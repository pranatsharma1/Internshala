# Generated by Django 2.2.5 on 2019-09-12 14:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190912_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 12, 19, 33, 2, 159005), verbose_name='date published'),
        ),
    ]
