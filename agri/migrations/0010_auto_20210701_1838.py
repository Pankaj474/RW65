# Generated by Django 3.1.1 on 2021-07-01 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0009_auto_20210701_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='long_lat',
            field=models.JSONField(blank=True, null=True),
        ),
    ]