# Generated by Django 4.2.5 on 2023-09-27 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='profile')),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('specialization', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='profile')),
                ('gender', models.CharField(max_length=10)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=200)),
                ('symptoms', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointmentdate', models.DateField()),
                ('appointmenttime', models.TimeField()),
                ('description', models.TextField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HospitalManagement.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HospitalManagement.patient')),
            ],
        ),
    ]
