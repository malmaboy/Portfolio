# Generated by Django 4.0.4 on 2022-05-25 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_delete_nonprogramminglanguages_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='NonProgrammingLanguages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
    ]
