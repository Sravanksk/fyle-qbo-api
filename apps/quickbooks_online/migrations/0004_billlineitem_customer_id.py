# Generated by Django 3.0.3 on 2020-02-15 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickbooks_online', '0003_auto_20200117_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='billlineitem',
            name='customer_id',
            field=models.CharField(help_text='QBO customer id', max_length=255, null=True),
        ),
    ]
