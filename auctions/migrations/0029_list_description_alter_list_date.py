# Generated by Django 4.0.1 on 2022-02-14 09:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0028_alter_list_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 14, 9, 0, 50, 957987, tzinfo=utc)),
        ),
    ]