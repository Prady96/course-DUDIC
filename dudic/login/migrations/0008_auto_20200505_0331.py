# Generated by Django 2.2 on 2020-05-05 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20200505_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationmodel',
            name='course_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='login.CourseModel'),
        ),
    ]
