# Generated by Django 5.1.1 on 2024-09-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0007_rename_adress_profile_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover_images',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='Images_Profile'),
        ),
    ]
