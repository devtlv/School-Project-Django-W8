# Generated by Django 3.1.4 on 2020-12-08 10:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0008_auto_20201208_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('questions', models.ManyToManyField(to='exams.Question')),
            ],
        ),
    ]