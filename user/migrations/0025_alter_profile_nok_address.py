# Generated by Django 4.1.3 on 2022-12-21 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0024_alter_beneficiary_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nok_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
