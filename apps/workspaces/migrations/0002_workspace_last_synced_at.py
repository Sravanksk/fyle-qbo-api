# Generated by Django 3.0.2 on 2020-01-31 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workspace',
            name='last_synced_at',
            field=models.DateTimeField(help_text='Datetime when expenses were pulled last', null=True),
        ),
    ]
