# Generated by Django 4.0.4 on 2022-04-28 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_blog_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_uz', models.CharField(max_length=255, verbose_name='Адресс [uz]')),
                ('address_ru', models.CharField(max_length=255, verbose_name='Адресс [ru]')),
                ('address_en', models.CharField(max_length=255, verbose_name='Адресс [en]')),
                ('email', models.CharField(max_length=255, verbose_name='Телефон')),
                ('contact_title_uz', models.CharField(default='Bog`lanish', max_length=255, verbose_name='Заголовок [uz]')),
                ('contact_title_ru', models.CharField(default='Контакты', max_length=255, verbose_name='Заголовок [ru]')),
                ('contact_title_en', models.CharField(default='Contuct us', max_length=255, verbose_name='Заголовок [en]')),
                ('contact_subtitle_uz', models.CharField(default='Agar sizda biron bir savol bo`lsa, quyidagi aloqa ma`lumotlaridan foydalaning.', max_length=255, verbose_name='Описание [uz]')),
                ('contact_subtitle_ru', models.CharField(default='Если у вас есть какие-либо вопросы, просто используйте следующие контактные данные.', max_length=255, verbose_name='Описание [ru]')),
                ('contact_subtitle_en', models.CharField(default='If you have any questions simply use the following contact details.', max_length=255, verbose_name='Описание [en]')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Почта',
                'verbose_name_plural': 'Почтовые адреса',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Номер',
                'verbose_name_plural': 'Контактные номеры',
            },
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Блог', 'verbose_name_plural': 'Блог'},
        ),
    ]
