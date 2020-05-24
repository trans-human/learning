# Generated by Django 2.2 on 2020-05-21 09:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200521_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approve_comments',
            new_name='approved_comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 9, 54, 20, 386201, tzinfo=utc)),
        ),
    ]
