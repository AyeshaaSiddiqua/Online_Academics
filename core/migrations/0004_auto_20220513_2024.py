# Generated by Django 3.1.4 on 2022-05-13 14:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210112_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 13, 14, 54, 7, 506700, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='exam',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 13, 14, 54, 7, 506700, tzinfo=utc)),
        ),
    ]
