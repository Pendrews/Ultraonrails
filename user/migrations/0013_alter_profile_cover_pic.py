# Generated by Django 4.1.3 on 2022-12-07 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_profile_res_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover_pic',
            field=models.ImageField(default='coveres.jpeg', upload_to='cover-pics'),
        ),
    ]