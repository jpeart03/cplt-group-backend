# Generated by Django 3.2.7 on 2021-09-29 01:08

import django.contrib.auth.models
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0009_alter_appuser_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='appuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='sent_to_email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='message',
            name='sent_to_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region=None),
        ),
    ]
