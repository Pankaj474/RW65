# Generated by Django 3.1.1 on 2021-06-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yard', '0028_settings_show_price_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='settings',
            name='show_price_group',
        ),
    ]
