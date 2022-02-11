# Generated by Django 4.0.1 on 2022-02-11 04:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_product_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='list',
            name='item',
        ),
        migrations.AddField(
            model_name='list',
            name='category',
            field=models.TextField(default=None, max_length=72),
        ),
        migrations.AddField(
            model_name='list',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 11, 12, 25, 56, 397257)),
        ),
        migrations.AddField(
            model_name='list',
            name='image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=32),
        ),
        migrations.AddField(
            model_name='list',
            name='title',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='user',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AlterField(
            model_name='bids',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.list'),
        ),
        migrations.AlterField(
            model_name='list',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.list'),
        ),
    ]
