# Generated by Django 3.1.5 on 2021-02-01 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210130_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
