# Generated by Django 3.1.1 on 2021-04-25 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yard', '0003_auto_20210422_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_weight2',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='price1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='price2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='price3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='price4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='price5',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='maximum_gross_weight',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='price_group',
            field=models.CharField(choices=[('price1', 'Price 1'), ('price2', 'Price 2'), ('price3', 'Price 3'), ('price4', 'Price 4'), ('price5', 'Price 5')], max_length=10),
        ),
    ]
