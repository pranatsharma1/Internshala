# Generated by Django 2.2.4 on 2019-09-12 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190912_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 12, 17, 6, 29, 667453), verbose_name='date published'),
        ),
    ]
