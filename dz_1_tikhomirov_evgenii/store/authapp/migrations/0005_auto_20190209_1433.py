# Generated by Django 2.1.5 on 2019-02-09 13:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20190202_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='active_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 11, 13, 33, 8, 4402, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
