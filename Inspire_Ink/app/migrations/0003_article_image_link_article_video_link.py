# Generated by Django 5.1.5 on 2025-01-24 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_article_tags_remove_article_views_view_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='video_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
