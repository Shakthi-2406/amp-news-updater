# Generated by Django 4.0 on 2022-02-04 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0004_rename_article_name_slide_article_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
