# Generated by Django 3.1.1 on 2021-06-17 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yard', '0027_trafficlight'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='show_price_group',
            field=models.BooleanField(default=False),
        ),
    ]