# Generated by Django 5.0.6 on 2024-07-05 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0014_remove_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default='admin', max_length=50),
            preserve_default=False,
        ),
    ]