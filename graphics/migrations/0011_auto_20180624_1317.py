# Generated by Django 2.0.6 on 2018-06-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphics', '0010_auto_20180624_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
