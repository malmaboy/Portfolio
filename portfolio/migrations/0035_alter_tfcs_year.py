# Generated by Django 4.0.5 on 2022-06-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0034_tfcs_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tfcs',
            name='year',
            field=models.DateField(),
        ),
    ]
