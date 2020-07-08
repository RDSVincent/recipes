# Generated by Django 3.0.7 on 2020-06-25 19:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0056_auto_20200625_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipeingredient',
            old_name='ingredient',
            new_name='food',
        ),
        migrations.AlterField(
            model_name='sharelink',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('4a604ec8-c158-4011-ab5d-ddad7604c1e3')),
        ),
    ]
