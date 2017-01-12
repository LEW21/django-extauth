# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import django_extauth.contrib.gitlab.profile


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(editable=False, max_length=150, unique=True, verbose_name='username')),
                ('last_login', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='last login')),
            ],
            bases=(models.Model, django_extauth.contrib.gitlab.profile.UserProfileMixin),
        ),
    ]
