# Generated by Django 4.1.5 on 2023-01-06 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shpargalka", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categoryarticle",
            name="description",
            field=models.TextField(blank=True, verbose_name="Описание категории"),
        ),
    ]
