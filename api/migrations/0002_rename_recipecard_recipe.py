# Generated by Django 4.1 on 2022-08-25 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecipeCard',
            new_name='Recipe',
        ),
    ]
