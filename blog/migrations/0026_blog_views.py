# Generated by Django 4.2.4 on 2024-03-01 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_alter_blog_options_selectedblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]