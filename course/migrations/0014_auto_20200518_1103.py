# Generated by Django 2.2 on 2020-05-18 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_auto_20200518_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='description',
            field=models.TextField(blank=True, default=' '),
        ),
    ]
