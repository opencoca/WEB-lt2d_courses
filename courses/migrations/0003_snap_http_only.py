# Generated by Django 3.1.7 on 2021-02-19 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20210211_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='snap',
            name='http_only',
            field=models.BooleanField(default=False),
        ),
    ]