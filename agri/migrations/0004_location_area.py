# Generated by Django 3.1.1 on 2021-06-25 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0003_auto_20210624_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='area',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
