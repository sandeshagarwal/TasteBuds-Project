# Generated by Django 5.0.6 on 2024-07-05 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_recipe_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]