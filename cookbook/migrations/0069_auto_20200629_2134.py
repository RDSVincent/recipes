# Generated by Django 3.0.7 on 2020-06-29 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0068_auto_20200629_2127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='header',
            new_name='is_header',
        ),
    ]
