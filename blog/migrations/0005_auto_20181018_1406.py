# Generated by Django 2.0.6 on 2018-10-18 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181018_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='commentlike',
            name='author',
        ),
        migrations.RemoveField(
            model_name='commentlike',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='postlike',
            name='author',
        ),
        migrations.RemoveField(
            model_name='postlike',
            name='post',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='CommentLike',
        ),
        migrations.DeleteModel(
            name='PostLike',
        ),
    ]