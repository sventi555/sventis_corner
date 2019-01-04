# Generated by Django 2.1.5 on 2019-01-04 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Graphic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140, unique=True)),
                ('link', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]