# Generated by Django 2.2.4 on 2019-09-14 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190914_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 14, 22, 19, 3, 181616), verbose_name='date published'),
        ),
    ]
