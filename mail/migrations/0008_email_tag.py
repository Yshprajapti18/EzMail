# Generated by Django 5.0.1 on 2024-02-16 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0007_alter_email_recipients_alter_email_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='tag',
            field=models.CharField(default='Personal', max_length=50),
            preserve_default=False,
        ),
    ]
