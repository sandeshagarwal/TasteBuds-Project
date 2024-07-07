# Generated by Django 5.0.6 on 2024-07-07 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0020_alter_recipe_author_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]