# Generated by Django 2.2 on 2020-05-06 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20200506_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationmodel',
            name='student_details',
            field=models.CharField(choices=[('ER', 'Entrepreneur'), ('UG', 'Undergraduate'), ('PG', 'Postgraduate')], default='none', max_length=2),
        ),
    ]
