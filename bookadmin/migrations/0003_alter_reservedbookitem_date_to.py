# Generated by Django 4.1.2 on 2022-10-21 23:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookadmin', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservedbookitem',
            name='date_to',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 10, 29, 5, 22, 53, 174383)),
        ),
    ]
