# Generated by Django 4.2.5 on 2023-09-27 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalManagement', '0003_remove_doctor_image_doctor_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='profile',
        ),
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='profile'),
        ),
    ]
