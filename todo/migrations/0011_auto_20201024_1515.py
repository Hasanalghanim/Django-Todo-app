# Generated by Django 3.1.2 on 2020-10-24 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_auto_20201022_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='datecompleted',
            field=models.DateTimeField(null=True),
        ),
    ]
