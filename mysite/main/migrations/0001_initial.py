# Generated by Django 2.2.5 on 2020-01-01 11:07

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_employer', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('image', models.ImageField(default='', upload_to='pics')),
                ('college_name', models.CharField(default='', max_length=200)),
                ('basic_skills', models.TextField(default='')),
                ('city', models.CharField(default='', max_length=200)),
                ('year_of_study', models.CharField(default='', max_length=200)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='JobStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accept', models.BooleanField(default=False)),
                ('is_reject', models.BooleanField(default=False)),
                ('intern_name', models.CharField(default='', max_length=200)),
                ('company_name', models.CharField(default='', max_length=100)),
                ('hire', models.CharField(default='', max_length=200)),
                ('available', models.CharField(default='', max_length=200)),
                ('job_title', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('category', models.CharField(default='', max_length=200)),
                ('location', models.CharField(default='', max_length=200)),
                ('job_duration', models.CharField(max_length=200)),
                ('job_content', models.TextField()),
                ('job_published', models.DateTimeField(default=datetime.datetime(2020, 1, 1, 16, 37, 49, 352472), verbose_name='date published')),
                ('job_stipend', models.CharField(max_length=200)),
                ('user', models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intern_name', models.CharField(default='', max_length=200)),
                ('hire', models.CharField(default='', max_length=200)),
                ('available', models.CharField(default='', max_length=200)),
                ('job_title', models.CharField(default='', max_length=200)),
                ('job_id', models.CharField(default='', max_length=100)),
                ('company_name', models.CharField(default='', max_length=100)),
                ('document', models.FileField(upload_to='documents/')),
                ('phone_no', models.CharField(max_length=10)),
                ('is_accept', models.BooleanField(default=False)),
                ('is_reject', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('username', models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
