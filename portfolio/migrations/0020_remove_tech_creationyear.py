# Generated by Django 4.0.4 on 2022-06-03 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_alter_tech_creationyear'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tech',
            name='creationYear',
        ),
    ]
