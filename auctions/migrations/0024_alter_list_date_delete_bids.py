# Generated by Django 4.0.1 on 2022-02-13 09:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_alter_list_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 13, 9, 55, 56, 324737, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Bids',
        ),
    ]