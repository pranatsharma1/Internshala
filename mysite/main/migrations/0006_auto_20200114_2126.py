# Generated by Django 2.2.5 on 2020-01-14 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200114_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intern',
            name='username',
        ),
        migrations.AlterField(
            model_name='job',
            name='job_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 14, 21, 26, 16, 855459), verbose_name='date published'),
        ),
    ]