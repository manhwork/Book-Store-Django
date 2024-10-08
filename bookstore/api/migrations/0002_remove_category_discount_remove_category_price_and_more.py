# Generated by Django 5.1.1 on 2024-09-26 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='category',
            name='price',
        ),
        migrations.RemoveField(
            model_name='category',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='./media/category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='./media/product'),
        ),
    ]
