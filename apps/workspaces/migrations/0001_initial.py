# Generated by Django 3.0.3 on 2020-03-10 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.AutoField(help_text='Unique Id to identify a workspace', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the workspace', max_length=255)),
                ('fyle_org_id', models.CharField(help_text='org id', max_length=255)),
                ('qbo_realm_id', models.CharField(help_text='qbo realm id', max_length=255)),
                ('last_synced_at', models.DateTimeField(help_text='Datetime when expenses were pulled last', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated at datetime')),
                ('user', models.ManyToManyField(help_text='Reference to users table', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkspaceSchedule',
            fields=[
                ('id', models.AutoField(help_text='Unique Id to identify a schedule', primary_key=True, serialize=False)),
                ('enabled', models.BooleanField(default=False)),
                ('start_datetime', models.DateTimeField(help_text='Datetime for start of schedule', null=True)),
                ('interval_hours', models.IntegerField(null=True)),
                ('fyle_job_id', models.CharField(max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkspaceSettings',
            fields=[
                ('id', models.AutoField(help_text='Unique Id to identify a workspace settings', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated at')),
                ('schedule', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='workspaces.WorkspaceSchedule')),
                ('workspace', models.OneToOneField(help_text='Reference to Workspace model', on_delete=django.db.models.deletion.PROTECT, to='workspaces.Workspace')),
            ],
        ),
        migrations.CreateModel(
            name='QBOCredential',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('refresh_token', models.TextField(help_text='Stores QBO refresh token')),
                ('realm_id', models.CharField(help_text='QBO realm / company Id', max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated at datetime')),
                ('workspace', models.OneToOneField(help_text='Reference to Workspace model', on_delete=django.db.models.deletion.PROTECT, to='workspaces.Workspace')),
            ],
        ),
        migrations.CreateModel(
            name='FyleCredential',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('refresh_token', models.TextField(help_text='Stores Fyle refresh token')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated at datetime')),
                ('workspace', models.OneToOneField(help_text='Reference to Workspace model', on_delete=django.db.models.deletion.PROTECT, to='workspaces.Workspace')),
            ],
        ),
    ]
