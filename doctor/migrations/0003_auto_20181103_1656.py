# Generated by Django 2.1.2 on 2018-11-03 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_doctor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='doctor/'),
        ),
    ]
