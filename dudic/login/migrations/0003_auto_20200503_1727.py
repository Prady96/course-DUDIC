# Generated by Django 2.2 on 2020-05-03 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0002_auto_20200502_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('education', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('mobile_num', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('reason', models.CharField(max_length=500)),
                ('hear_about', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Application',
                'verbose_name_plural': 'Applications',
            },
        ),
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='DateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='login.CourseModel')),
            ],
            options={
                'verbose_name': 'Date',
                'verbose_name_plural': 'Dates',
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('education', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('mobile_num', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('reason', models.CharField(max_length=500)),
                ('hear_about', models.CharField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.DeleteModel(
            name='ApplyModel',
        ),
        migrations.AddField(
            model_name='applicationmodel',
            name='course_date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='login.DateModel'),
        ),
        migrations.AddField(
            model_name='applicationmodel',
            name='course_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='login.CourseModel'),
        ),
    ]
