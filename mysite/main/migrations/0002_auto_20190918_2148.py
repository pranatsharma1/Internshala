# Generated by Django 2.2.5 on 2019-09-18 16:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 18, 21, 48, 20, 613009), verbose_name='date published'),
        ),
    ]
