# Generated by Django 2.1.5 on 2019-01-04 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='graphic',
            old_name='link',
            new_name='iframe',
        ),
    ]
