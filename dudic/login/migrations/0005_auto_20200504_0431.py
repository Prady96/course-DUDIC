# Generated by Django 2.2 on 2020-05-04 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20200503_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datemodel',
            name='course',
        ),
        migrations.AddField(
            model_name='datemodel',
            name='course_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='login.CourseModel'),
        ),
    ]
