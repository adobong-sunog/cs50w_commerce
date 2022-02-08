# Generated by Django 4.0.1 on 2022-02-08 11:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='list',
            name='user',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='list',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 8, 19, 17, 55, 727562)),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=11),
        ),
    ]