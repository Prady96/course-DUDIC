# Generated by Django 2.2 on 2020-05-15 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_lecture_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='meeting_timing',
            field=models.CharField(max_length=10, null=True),
        ),
    ]