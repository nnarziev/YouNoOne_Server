# Generated by Django 2.2.1 on 2019-06-01 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20190601_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='heartbeat_smartphone',
            field=models.BigIntegerField(blank=True, default=1559384505.137416),
        ),
        migrations.AlterField(
            model_name='participant',
            name='heartbeat_smartwatch',
            field=models.BigIntegerField(blank=True, default=1559384505.137416),
        ),
        migrations.AlterField(
            model_name='participant',
            name='last_login_datetime',
            field=models.BigIntegerField(blank=True, default=1559384505.137416),
        ),
        migrations.AlterField(
            model_name='participant',
            name='register_datetime',
            field=models.BigIntegerField(blank=True, default=1559384505.137416),
        ),
    ]