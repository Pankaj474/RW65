# Generated by Django 3.1.1 on 2021-06-27 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0005_cropcycle_cycle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cropcycle',
            name='start_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
