# Generated by Django 5.1.5 on 2025-02-03 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nosotros',
            name='imagen',
            field=models.ImageField(default='default.jpg', upload_to='nosotros/'),
        ),
    ]
