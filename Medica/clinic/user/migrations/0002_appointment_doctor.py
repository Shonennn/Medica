# Generated by Django 4.1.2 on 2022-11-07 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=32)),
                ('phone_number', models.CharField(max_length=32)),
                ('date', models.DateField()),
                ('comment', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('introduction', models.CharField(max_length=255)),
                ('picture', models.CharField(max_length=255)),
            ],
        ),
    ]
