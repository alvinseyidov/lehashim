# Generated by Django 4.2.4 on 2023-12-11 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_blogcategory_publish_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategory',
            name='publish_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
