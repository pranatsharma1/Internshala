# Generated by Django 2.2.5 on 2021-08-28 00:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210827_2356'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Application_Status',
        ),
        migrations.AlterField(
            model_name='job',
            name='job_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 28, 5, 48, 53, 494591), verbose_name='date published'),
        ),
    ]
