# Generated by Django 3.1.7 on 2021-02-21 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ImageField(default=None, upload_to='images'),
        ),
    ]
