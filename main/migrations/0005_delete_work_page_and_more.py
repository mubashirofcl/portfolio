# Generated by Django 5.0.3 on 2024-04-24 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_projectpage_project_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Work_page',
        ),
        migrations.RenameField(
            model_name='projectpage',
            old_name='project_languages',
            new_name='project_languages_urls',
        ),
    ]
