# Generated by Django 4.2.4 on 2023-12-11 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_remove_servicecategory_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='category',
        ),
        migrations.DeleteModel(
            name='ServiceCategory',
        ),
    ]
