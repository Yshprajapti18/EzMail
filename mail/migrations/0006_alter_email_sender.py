# Generated by Django 5.0.1 on 2024-02-11 14:32

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0005_alter_email_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='sender',
            field=models.EmailField(default=django.contrib.auth.models.User, max_length=254),
        ),
    ]
