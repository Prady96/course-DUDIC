# Generated by Django 2.2 on 2020-05-17 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_lecture_lecture_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slack_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]