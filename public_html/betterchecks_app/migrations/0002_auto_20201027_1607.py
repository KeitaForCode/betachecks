# Generated by Django 3.0.3 on 2020-10-27 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betterchecks_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]