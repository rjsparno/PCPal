# Generated by Django 2.0.7 on 2018-07-13 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PCPal', '0010_hdd'),
    ]

    operations = [
        migrations.CreateModel(
            name='PSU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('psu_name', models.CharField(max_length=200)),
                ('psu_price', models.CharField(max_length=200)),
                ('psu_watts', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TWR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twr_name', models.CharField(max_length=200)),
                ('twr_price', models.CharField(max_length=200)),
                ('twr_type', models.CharField(max_length=200)),
            ],
        ),
    ]
