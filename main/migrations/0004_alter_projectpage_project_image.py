# Generated by Django 5.0.3 on 2024-04-12 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_project_page_projectpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='project_image',
            field=models.ImageField(upload_to='projectPage'),
        ),
    ]