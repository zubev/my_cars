# Generated by Django 3.1.5 on 2021-02-04 16:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_auto_20210202_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1960), django.core.validators.MaxValueValidator(2022)]),
        ),
    ]
