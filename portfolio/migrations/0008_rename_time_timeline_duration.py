# Generated by Django 4.2.4 on 2023-08-24 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_timeline_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timeline',
            old_name='time',
            new_name='duration',
        ),
    ]
