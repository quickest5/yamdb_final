# Generated by Django 3.2 on 2023-03-09 11:59

import api.validators
import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221222_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'Пользователь'), ('moderator', 'Модератор'), ('admin', 'Админ')], default='user', max_length=9),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[api.validators.validate_username, django.contrib.auth.validators.UnicodeUsernameValidator()]),
        ),
    ]
