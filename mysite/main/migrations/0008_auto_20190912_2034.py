# Generated by Django 2.2.4 on 2019-09-12 15:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190912_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 12, 20, 34, 17, 265708), verbose_name='date published'),
        ),
        migrations.CreateModel(
            name='profile_m',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
    ]