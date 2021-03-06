# Generated by Django 4.0.4 on 2022-05-31 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_remove_tech_img_tech_imglink'),
    ]

    operations = [
        migrations.CreateModel(
            name='labs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.TextField(default='nothing')),
                ('description', models.TextField(default='Description')),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(default='Text')),
                ('imgLink', models.TextField(default='link')),
            ],
        ),
    ]
