# Generated by Django 2.2.1 on 2019-05-24 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20190524_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='staff_picture',
            field=models.ImageField(blank=True, height_field=30, null=True, upload_to='uploaded_images', width_field=30),
        ),
    ]
