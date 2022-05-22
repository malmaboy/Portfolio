# Generated by Django 4.0.4 on 2022-05-20 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammingLanguages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=50)),
                ('projectLink', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectName', models.CharField(max_length=50)),
                ('year', models.IntegerField(default=1)),
                ('semester', models.IntegerField(default=1)),
                ('ects', models.IntegerField(default=4)),
                ('lective_Year', models.CharField(max_length=10)),
                ('rank', models.IntegerField(default=1)),
                ('professor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topicsName', models.CharField(max_length=40)),
            ],
        ),
    ]
