# Generated by Django 5.0.1 on 2024-02-16 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0008_email_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='tag',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
