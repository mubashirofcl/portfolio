# Generated by Django 5.0.3 on 2024-04-24 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_delete_work_page_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectpage',
            old_name='project_languages_urls',
            new_name='project_languages_urls1',
        ),
        migrations.AddField(
            model_name='projectpage',
            name='project_languages_urls2',
            field=models.CharField(default='#', max_length=255),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='project_languages_urls3',
            field=models.CharField(default='#', max_length=255),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='project_languages_urls4',
            field=models.CharField(default='#', max_length=255),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='project_languages_urls5',
            field=models.CharField(default='#', max_length=255),
        ),
    ]