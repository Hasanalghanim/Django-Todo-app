# Generated by Django 3.1.2 on 2020-10-23 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20201022_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created',
        ),
    ]
