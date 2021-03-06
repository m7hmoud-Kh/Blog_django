# Generated by Django 3.2.9 on 2021-12-27 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_first', models.CharField(max_length=100)),
                ('user_last', models.CharField(max_length=100)),
                ('user_img', models.ImageField(upload_to='photo/')),
                ('user_email', models.EmailField(max_length=254)),
                ('user_pass', models.CharField(max_length=50)),
                ('user_date_on', models.DateField(default=datetime.datetime(2021, 12, 27, 20, 38, 43, 691974))),
            ],
        ),
    ]
