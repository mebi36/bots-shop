# Generated by Django 4.1.1 on 2022-09-21 04:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0003_alter_client_date_joined"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="date_joined",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 9, 21, 4, 29, 22, 771923, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
