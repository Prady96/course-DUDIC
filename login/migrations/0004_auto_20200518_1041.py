# Generated by Django 2.2 on 2020-05-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200518_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='course_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='date',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
