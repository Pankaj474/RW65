# Generated by Django 3.1.1 on 2021-06-02 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yard', '0011_auto_20210515_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='license_plate',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
