# Generated by Django 5.0.3 on 2024-04-12 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_project_page_remove_work_page_work_main_diss'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project_page',
            new_name='projectPage',
        ),
    ]