# Generated by Django 2.2 on 2020-05-18 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_auto_20200518_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='download_resources',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
