# Generated by Django 4.0.5 on 2022-06-05 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0026_alter_labs_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogsanswers',
            name='imageUrl',
        ),
        migrations.RemoveField(
            model_name='news',
            name='imgLink',
        ),
        migrations.RemoveField(
            model_name='tech',
            name='imageUrl',
        ),
        migrations.AddField(
            model_name='blogsanswers',
            name='image',
            field=models.ImageField(default=1, upload_to='blogImages/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default='null', upload_to='newsImages/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tech',
            name='image',
            field=models.ImageField(default='null', upload_to='TechImages/'),
            preserve_default=False,
        ),
    ]