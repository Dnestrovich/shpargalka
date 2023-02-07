# Generated by Django 4.1.5 on 2023-01-22 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shpargalka", "0014_articletree_delete_categorypost_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="articletree",
            options={
                "ordering": ("category_article", "number_post"),
                "verbose_name": "-Статья tree",
                "verbose_name_plural": "-- Статьи tree",
            },
        ),
        migrations.AlterModelOptions(
            name="categorytreearticle",
            options={
                "ordering": ("tree_id", "level"),
                "verbose_name": "-Категория (Tree)",
                "verbose_name_plural": "-- Категории (Tree)",
            },
        ),
    ]
