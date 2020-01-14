# Generated by Django 2.2.5 on 2020-01-11 20:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200112_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='intern',
            name='basic_skills',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='intern',
            name='city',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='intern',
            name='college_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='intern',
            name='year_of_study',
            field=models.IntegerField(choices=[(1, 'first_year'), (2, 'second_year'), (3, 'third_year'), (4, 'fourth_year')], default=1),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 12, 2, 7, 22, 528262), verbose_name='date published'),
        ),
    ]