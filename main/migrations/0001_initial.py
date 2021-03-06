# Generated by Django 4.0.3 on 2022-04-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Задний фон')),
                ('title_uz', models.TextField(verbose_name='Заголовок [uz]')),
                ('title_ru', models.TextField(verbose_name='Заголовок [ru]')),
                ('title_en', models.TextField(verbose_name='Заголовок [en]')),
                ('subtitle_uz', models.TextField(verbose_name='Подзаголовок [uz]')),
                ('subtitle_ru', models.TextField(verbose_name='Подзаголовок [ru]')),
                ('subtitle_en', models.TextField(verbose_name='Подзаголовок [en]')),
            ],
        ),
    ]
