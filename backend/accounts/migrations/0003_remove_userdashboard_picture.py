# Generated by Django 4.2.5 on 2024-03-01 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userdashboard_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdashboard',
            name='picture',
        ),
    ]