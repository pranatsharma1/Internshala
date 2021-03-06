# Generated by Django 2.2.5 on 2019-09-22 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190922_1123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='username',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='intern',
            name='intern_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 22, 15, 22, 13, 78602), verbose_name='date published'),
        ),
    ]
