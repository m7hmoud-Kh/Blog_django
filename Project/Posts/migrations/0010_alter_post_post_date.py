# Generated by Django 3.2.9 on 2021-12-28 21:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0009_alter_post_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateField(default=datetime.datetime(2021, 12, 28, 23, 12, 21, 685478)),
        ),
    ]
