# Generated by Django 3.1.1 on 2021-03-04 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('ip_addr', models.CharField(max_length=100)),
                ('serial_num', models.CharField(default='None', max_length=100)),
                ('mac_addr', models.CharField(max_length=100)),
                ('port', models.PositiveIntegerField(blank=True)),
                ('wx_btn', models.BooleanField(default=True)),
                ('zero_btn', models.BooleanField(default=True)),
                ('tara_btn', models.BooleanField(default=True)),
                ('man_tara_btn', models.BooleanField(default=True)),
                ('x10_btn', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=False)),
                ('certi_num', models.CharField(default='None', max_length=100)),
                ('max_weight', models.PositiveIntegerField(blank=True, null=True)),
                ('min_weight', models.PositiveIntegerField(blank=True, null=True)),
                ('e_d', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
                ('updated_date_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('trans_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
                ('updated_date_time', models.DateTimeField(auto_now=True)),
                ('tara', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('net_weight', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scale_app.devices')),
            ],
        ),
    ]