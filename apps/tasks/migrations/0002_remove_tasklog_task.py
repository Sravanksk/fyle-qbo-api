# Generated by Django 3.0.2 on 2020-01-13 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklog',
            name='task',
        ),
    ]