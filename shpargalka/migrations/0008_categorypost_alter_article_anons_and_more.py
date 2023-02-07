# Generated by Django 4.1.5 on 2023-01-12 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shpargalka", "0007_alter_article_image_article"),
    ]

    operations = [
        migrations.CreateModel(
            name="CategoryPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name_cat",
                    models.CharField(max_length=150, verbose_name="Категория поста"),
                ),
                ("slug_cat", models.SlugField(max_length=160, unique=True)),
                (
                    "description_cat",
                    models.TextField(blank=True, verbose_name="Описание категории"),
                ),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
            ],
            options={"verbose_name": "Категория", "verbose_name_plural": "Категории",},
        ),
        migrations.AlterField(
            model_name="article",
            name="anons",
            field=models.TextField(blank=True, verbose_name="Анонс"),
        ),
        migrations.AlterField(
            model_name="article",
            name="full_text",
            field=models.TextField(blank=True, verbose_name="Статья"),
        ),
    ]
