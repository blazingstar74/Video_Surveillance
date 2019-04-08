# Generated by Django 2.0 on 2019-04-03 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='idconfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terminal_id', models.CharField(max_length=64)),
                ('res_id', models.CharField(max_length=64)),
                ('config', models.CharField(max_length=1000)),
                ('capturedserver', models.CharField(max_length=200)),
                ('interval', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='rtsp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terminal_id', models.CharField(max_length=64)),
                ('res_id', models.CharField(max_length=64)),
                ('res_name', models.CharField(max_length=200)),
                ('camid', models.CharField(max_length=200)),
                ('rtsp', models.CharField(max_length=1000)),
                ('cam_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_password', models.CharField(max_length=200)),
            ],
        ),
    ]