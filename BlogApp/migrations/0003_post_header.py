# Generated by Django 4.0.4 on 2022-04-19 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_post_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
