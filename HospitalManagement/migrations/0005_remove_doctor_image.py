# Generated by Django 4.2.5 on 2023-09-27 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalManagement', '0004_remove_doctor_profile_doctor_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='image',
        ),
    ]