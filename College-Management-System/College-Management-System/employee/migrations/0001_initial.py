# Generated by Django 4.2.1 on 2023-05-23 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_number', models.CharField(max_length=20)),
                ('register_date', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('another_name', models.CharField(max_length=100)),
                ('nid', models.IntegerField()),
                ('employee_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='OfficialInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('official_register_number', models.CharField(max_length=20)),
                ('official_register_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('another_fullname', models.CharField(max_length=100)),
                ('national_id', models.IntegerField()),
                ('employee_avatar', models.ImageField(upload_to='photos/%Y/%m/%d/')),
            ],
        ),
    ]
