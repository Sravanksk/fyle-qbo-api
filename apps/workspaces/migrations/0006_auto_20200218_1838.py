# Generated by Django 3.0.3 on 2020-02-18 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0005_workspacesettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='workspacesettings',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=None, help_text='Created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workspacesettings',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Updated at'),
        ),
    ]
