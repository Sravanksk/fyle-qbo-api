# Generated by Django 3.0.3 on 2020-03-08 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0008_auto_20200221_1301'),
    ]

    operations = [
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
        migrations.RemoveField(
            model_name='workspacesettings',
            name='schedule_enabled',
        ),
        migrations.AlterField(
            model_name='workspacesettings',
            name='schedule',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='workspaces.WorkspaceSchedule'),
        ),
    ]
