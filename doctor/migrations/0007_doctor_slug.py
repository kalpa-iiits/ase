# Generated by Django 2.1.2 on 2018-11-03 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_doctor_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
