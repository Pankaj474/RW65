# Generated by Django 3.1.1 on 2021-06-29 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0006_auto_20210627_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='croptask',
            name='end_day',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='croptask',
            name='start_day',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
