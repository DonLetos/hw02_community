# Generated by Django 4.1.4 on 2023-01-30 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_group_post_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='titel',
            new_name='title',
        ),
    ]
