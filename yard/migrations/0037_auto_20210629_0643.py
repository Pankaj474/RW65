# Generated by Django 3.1.1 on 2021-06-29 06:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yard', '0036_auto_20210629_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='ss_role_access',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='buildingsite',
            name='ss_role_access',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customer',
            name='ss_role_access',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='supplier',
            name='ss_role_access',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='ss_role_access',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
