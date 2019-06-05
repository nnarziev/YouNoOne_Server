# Generated by Django 2.2.1 on 2019-06-01 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0005_auto_20190601_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='unlocked_dur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_endtime', models.BigIntegerField(default=0)),
                ('duration', models.TextField(blank=True, default='')),
                ('device', models.CharField(default='', max_length=10)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='step_detector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.BigIntegerField(default=0)),
                ('device', models.CharField(default='', max_length=10)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='stationary_dur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_endtime', models.BigIntegerField(default=0)),
                ('duration', models.TextField(blank=True, default='')),
                ('device', models.CharField(default='', max_length=10)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='significant_motion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.BigIntegerField(default=0)),
                ('device', models.CharField(default='', max_length=10)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='phone_calls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.BigIntegerField(default=0)),
                ('call_type', models.TextField(blank=True, default='')),
                ('duration', models.TextField(blank=True, default='')),
                ('device', models.CharField(default='', max_length=10)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='light_intensity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.BigIntegerField(default=0)),
                ('value', models.TextField(blank=True, default='')),
                ('device', models.CharField(default='', max_length=10)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='hrm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.BigIntegerField(default=0)),
                ('value', models.TextField(blank=True, default='')),
                ('device', models.CharField(default='', max_length=10)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='app_usage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.BigIntegerField(default=0)),
                ('app_name', models.TextField(blank=True, default='')),
                ('value', models.TextField(blank=True, default='')),
                ('device', models.CharField(default='', max_length=10)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='acc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.BigIntegerField(default=0)),
                ('value_x', models.TextField(blank=True, default='')),
                ('value_y', models.TextField(blank=True, default='')),
                ('value_z', models.TextField(blank=True, default='')),
                ('device', models.CharField(default='', max_length=10)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
    ]
