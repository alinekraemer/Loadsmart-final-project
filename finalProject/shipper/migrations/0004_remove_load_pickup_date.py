# Generated by Django 2.1.7 on 2019-03-27 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipper', '0003_auto_20190327_0528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='load',
            name='pickup_date',
        ),
    ]
