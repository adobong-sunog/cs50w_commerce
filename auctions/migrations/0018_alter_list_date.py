# Generated by Django 4.0.1 on 2022-02-11 11:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_alter_list_date_alter_list_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 11, 11, 36, 10, 60033, tzinfo=utc)),
        ),
    ]
