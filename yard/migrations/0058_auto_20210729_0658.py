# Generated by Django 3.1.1 on 2021-07-29 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yard', '0057_silo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='silo',
            name='yard',
        ),
        migrations.AddField(
            model_name='silo',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='yard.warehouse'),
        ),
        migrations.CreateModel(
            name='MaterialQuality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(choices=[('Quality A', 'Quality A'), ('Quality B', 'Quality B'), ('Quality C', 'Quality C')], max_length=100)),
                ('humidity', models.CharField(choices=[('Good', 'Good'), ('Average', 'Average'), ('Worse', 'Worse')], max_length=100)),
                ('Fertilizer', models.CharField(choices=[('A Grade', 'A Grade'), ('B Grade', 'B Grade'), ('C Grade', 'C Grade')], max_length=100)),
                ('Amount', models.IntegerField(blank=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yard.article')),
            ],
        ),
    ]
