# Generated by Django 4.2.3 on 2023-10-31 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blog_reading_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
    ]