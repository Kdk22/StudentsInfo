# Generated by Django 2.2.2 on 2019-06-23 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentInfo', '0005_auto_20190616_0537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='timer',
            new_name='time',
        ),
    ]
