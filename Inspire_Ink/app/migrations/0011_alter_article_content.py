# Generated by Django 5.1.5 on 2025-01-25 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_article_introduction_alter_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, help_text='The content of the article.', null=True),
        ),
    ]
