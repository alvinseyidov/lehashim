# Generated by Django 4.2.4 on 2024-02-17 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_review_alter_blog_options_alter_tag_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]