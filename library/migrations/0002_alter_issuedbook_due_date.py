# Generated by Django 4.2.13 on 2024-07-11 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 25, 18, 16, 40, 377197)),
        ),
    ]
