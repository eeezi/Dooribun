# Generated by Django 4.1 on 2022-08-17 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='head',
            field=models.IntegerField(default=2),
        ),
    ]
