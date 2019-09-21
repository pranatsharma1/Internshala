# Generated by Django 2.2.5 on 2019-09-21 19:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190922_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 22, 0, 44, 43, 774585), verbose_name='date published'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
