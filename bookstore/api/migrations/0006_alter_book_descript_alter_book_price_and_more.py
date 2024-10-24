# Generated by Django 5.1 on 2024-10-18 02:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_author_avatar_alter_blog_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='descript',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='book',
            name='stock',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
