# Generated by Django 4.2.4 on 2023-08-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_home_about_alter_home_file_alter_home_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='portfolio/files/'),
        ),
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio/images/'),
        ),
    ]