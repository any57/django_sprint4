# Generated by Django 3.2.16 on 2024-06-06 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='is_published',
        ),
    ]
