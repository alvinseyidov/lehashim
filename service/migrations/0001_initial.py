# Generated by Django 4.2.4 on 2024-03-10 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('sort', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Xidmət',
                'verbose_name_plural': 'Xidmətlər',
                'ordering': ('sort',),
            },
        ),
    ]
