# Generated by Django 4.0 on 2022-02-05 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0007_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('General', 'General'), ('Anime', 'Anime'), ('Sports', 'Sports'), ('Hollywood', 'Hollywood'), ('Bollyhood', 'Bollyhood'), ('Sports', 'Sports'), ('Netflix', 'Netflix')], default='Unknown', max_length=20),
        ),
    ]
