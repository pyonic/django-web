# Generated by Django 4.0.4 on 2022-04-28 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blog_alter_banner_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('news', 'Новости'), ('blog', 'Блог')], max_length=255, null=True, verbose_name='Категория'),
        ),
    ]
