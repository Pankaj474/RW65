# Generated by Django 3.1.1 on 2021-06-16 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yard', '0026_auto_20210615_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrafficLight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
