# Generated by Django 4.0.5 on 2022-06-05 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0028_projects_projectimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
