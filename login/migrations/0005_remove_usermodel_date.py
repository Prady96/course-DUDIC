# Generated by Django 2.2 on 2020-05-18 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20200518_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='date',
        ),
    ]