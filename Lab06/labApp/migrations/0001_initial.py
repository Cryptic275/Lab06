# Generated by Django 4.2.5 on 2023-10-28 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('studentName', models.CharField(max_length=128)),
                ('gpa', models.FloatField()),
                ('courses', models.ManyToManyField(blank=True, related_name='students', to='labApp.course')),
            ],
        ),
    ]
