# Generated by Django 2.2.5 on 2021-02-26 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20210225_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='room_picture'),
        ),
    ]
