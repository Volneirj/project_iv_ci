# Generated by Django 4.2.13 on 2024-08-09 20:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_alter_issuedbook_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 23, 20, 57, 35, 871316, tzinfo=datetime.timezone.utc)),
        ),
    ]
