# Generated by Django 4.0 on 2022-02-06 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotter_app', '0007_comments_parent_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]