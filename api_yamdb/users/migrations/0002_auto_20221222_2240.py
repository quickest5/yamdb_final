# Generated by Django 3.2 on 2022-12-22 22:40

import api.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[api.validators.validate_username, django.core.validators.RegexValidator(message='Ник содержит недопустимые символы', regex='^[\\w.@+-]+\\Z')]),
        ),
    ]