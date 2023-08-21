# Generated by Django 4.2.4 on 2023-08-21 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_maincategory_subcategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maincategory',
            options={'ordering': ('sort',)},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ('sort',)},
        ),
        migrations.AddField(
            model_name='maincategory',
            name='sort',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='sort',
            field=models.IntegerField(default=0),
        ),
    ]
