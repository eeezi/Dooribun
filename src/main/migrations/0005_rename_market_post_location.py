# Generated by Django 4.1 on 2022-08-17 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_location_post_market'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='market',
            new_name='location',
        ),
    ]