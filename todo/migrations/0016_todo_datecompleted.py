# Generated by Django 3.1.2 on 2020-10-24 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0015_auto_20201024_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='datecompleted',
            field=models.DateTimeField(null=True),
        ),
    ]