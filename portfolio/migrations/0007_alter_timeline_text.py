# Generated by Django 4.2.4 on 2023-08-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_alter_home_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]