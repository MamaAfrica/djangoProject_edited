# Generated by Django 2.2.1 on 2019-05-24 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='staff_id',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='staff_picture',
            field=models.ImageField(null=True, upload_to='', width_field=15),
        ),
        migrations.AddField(
            model_name='staff',
            name='staff_post',
            field=models.CharField(max_length=30, null=True),
        ),
    ]