# Generated by Django 2.2.2 on 2019-06-16 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentInfo', '0004_auto_20190616_0519'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='question',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='test',
            name='answer',
            field=models.CharField(max_length=1000),
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
