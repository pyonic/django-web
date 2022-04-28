# Generated by Django 4.0.4 on 2022-04-28 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('news', 'Новости'), ('blog', 'Блог')], default='blog', max_length=255, verbose_name='Категория'),
        ),
    ]
