# Generated by Django 2.0.6 on 2018-06-17 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphics', '0003_auto_20180617_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=None),
        ),
    ]
