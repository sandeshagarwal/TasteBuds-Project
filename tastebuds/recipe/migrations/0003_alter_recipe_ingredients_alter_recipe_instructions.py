# Generated by Django 5.0.6 on 2024-07-05 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_rename_instuctions_ingredient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='recipe.ingredient'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.ManyToManyField(to='recipe.instuction'),
        ),
    ]
