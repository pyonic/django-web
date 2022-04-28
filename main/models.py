from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone 


class MainData(models.Model):
	title = models.CharField(max_length = 255, verbose_name = 'Заголовок сайта')
	sitename = models.CharField(max_length = 255, verbose_name = 'Название учереждения')
	keywords = models.CharField(max_length = 255, verbose_name = 'Ключевые слова [SEO]')
	description = models.CharField(max_length = 255, verbose_name = 'Описание сайта [SEO]')
	worktime_uz = models.CharField(max_length = 255, verbose_name = 'Рабочее время [uz]')
	worktime_ru = models.CharField(max_length = 255, verbose_name = 'Рабочее время [ru]')
	worktime_en = models.CharField(max_length = 255, verbose_name = 'Рабочее время [en]')

	def __str__(self):
		return 'Основные настройки и данные сайта'

	def save(self, *args, **kwargs):
		if not self.pk and MainData.objects.exists():
			return 0
		return super(MainData, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Основное'
		verbose_name_plural = 'Основные'

class Banner(models.Model):
	image = models.ImageField(upload_to = 'images/', verbose_name='Задний фон')
	title_uz = models.TextField(verbose_name = 'Заголовок [uz]')
	title_ru = models.TextField(verbose_name = 'Заголовок [ru]')
	title_en = models.TextField(verbose_name = 'Заголовок [en]')
	subtitle_uz = models.TextField(verbose_name = 'Подзаголовок [uz]')
	subtitle_ru = models.TextField(verbose_name = 'Подзаголовок [ru]')
	subtitle_en = models.TextField(verbose_name = 'Подзаголовок [en]')

	def __str__(self):
		return self.title_ru

	class Meta:
		verbose_name = 'Баннер'
		verbose_name_plural = 'Баннер'

class Blog(models.Model):
	STATIC_CHOISES = (('draft','Черновик'),('published','Публикация'))
	CATEGORY_TYPES = (
		('news', 'Новости'),
		('blog', 'Блог')
	)
	category = models.CharField(max_length = 255,choices= CATEGORY_TYPES, verbose_name = 'Категория', default = 'blog')
	image = models.ImageField(upload_to = 'blog/', verbose_name='Фотография')
	author = models.TextField(verbose_name = 'Автор')
	title_uz = models.CharField(max_length = 255, verbose_name = 'Заголовок [uz]')
	title_ru = models.CharField(max_length = 255, verbose_name = 'Заголовок [ru]')
	title_en = models.CharField(max_length = 255, verbose_name = 'Заголовок [en]')
	description_uz = models.TextField(verbose_name = 'Описание [uz]')
	description_ru = models.TextField(verbose_name = 'Описание [ru]')
	description_en = models.TextField(verbose_name = 'Описание [en]')
	content_uz =  HTMLField(verbose_name = "Контент [uz]")
	content_ru =  HTMLField(verbose_name = "Контент [ru]")
	content_en =  HTMLField(verbose_name = "Контент [en]")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	publish = models.DateTimeField(default=timezone.now)
	slug = models.SlugField(max_length = 250,unique_for_date='publish', blank = True)
	status  = models.CharField(max_length=10,choices=STATIC_CHOISES,default='draft')
	
	class Meta:
		ordering     = ('-publish',)
		verbose_name = "Пост"
		verbose_name_plural = "Посты"

class Phone(models.Model):
	phone = models.CharField(max_length = 255, verbose_name = 'Телефон')

	def __str__(self):
		return self.phone

	class Meta:
		verbose_name = 'Номер'
		verbose_name_plural = 'Телефонные номера'

class Email(models.Model):
	email = models.CharField(max_length = 255, verbose_name = 'Почта')

	def __str__(self):
			return self.email

	class Meta:
		verbose_name = 'Почта'
		verbose_name_plural = 'Почтовые адреса'

class Adress(models.Model):
	address_uz = models.CharField(max_length = 255, verbose_name = 'Адресс [uz]')
	address_ru = models.CharField(max_length = 255, verbose_name = 'Адресс [ru]')
	address_en = models.CharField(max_length = 255, verbose_name = 'Адресс [en]')
	
	def __str__(self):
			return self.address_ru

	def save(self, *args, **kwargs):
		if not self.pk and Adress.objects.exists():
			return 0
		return super(Adress, self).save(*args, **kwargs)
		
	class Meta:
		verbose_name = 'Адрес'
		verbose_name_plural = 'Адреса'

class Contact(models.Model):
	contact_title_uz = models.CharField(max_length = 255, verbose_name = 'Заголовок [uz]', default = 'Bog`lanish')
	contact_title_ru = models.CharField(max_length = 255, verbose_name = 'Заголовок [ru]', default = 'Контакты')
	contact_title_en = models.CharField(max_length = 255, verbose_name = 'Заголовок [en]', default = 'Contuct us')
	contact_subtitle_uz = models.CharField(max_length = 255, verbose_name = 'Описание [uz]', default = 'Agar sizda biron bir savol bo`lsa, quyidagi aloqa ma`lumotlaridan foydalaning.')
	contact_subtitle_ru = models.CharField(max_length = 255, verbose_name = 'Описание [ru]', default = 'Если у вас есть какие-либо вопросы, просто используйте следующие контактные данные.')
	contact_subtitle_en = models.CharField(max_length = 255, verbose_name = 'Описание [en]', default = 'If you have any questions simply use the following contact details.')

	def __str__(self):
			return self.contact_title_ru

	class Meta:
		verbose_name = 'Контакт'
		verbose_name_plural = 'Контакты'

class About(models.Model):
	title_uz = models.CharField( max_length = 255, verbose_name = 'Заголовок [uz]')
	title_ru = models.CharField( max_length = 255, verbose_name = 'Заголовок [ru]')
	title_en = models.CharField( max_length = 255, verbose_name = 'Заголовок [en]')
	description_uz = models.TextField(verbose_name = 'Описание [uz]')
	description_ru = models.TextField(verbose_name = 'Описание [ru]')
	description_en = models.TextField(verbose_name = 'Описание [en]')
	slogan_uz = models.CharField( max_length = 255, verbose_name = 'Слоган [uz]')
	slogan_ru = models.CharField( max_length = 255, verbose_name = 'Слоган [ru]')
	slogan_en = models.CharField( max_length = 255, verbose_name = 'Слоган [en]')
	video = models.CharField( max_length = 500, verbose_name = 'Ссылка на видео')
	video_poster = models.ImageField(upload_to = 'images/', verbose_name='Фотография')
	background = models.ImageField(upload_to = 'images/', verbose_name='Задний фон шапки')

	def __str__(self):
		return self.title_ru
	
	class Meta:
		verbose_name = 'О нас'
		verbose_name_plural = 'О нас'

class Achievments(models.Model):
	count = models.CharField( max_length = 500, verbose_name = 'Количество')
	title_uz = models.CharField( max_length = 255, verbose_name = 'Заголовок [uz]')
	title_ru = models.CharField( max_length = 255, verbose_name = 'Заголовок [ru]')
	title_en = models.CharField( max_length = 255, verbose_name = 'Заголовок [en]')

	def __str__(self):
		return self.title_ru
	
	class Meta:
		verbose_name = 'Достижение'
		verbose_name_plural = 'Достижения'

class Socials(models.Model):
	SOCIAL_ICONS = (
		('fab fa-facebook-f', 'Facebook'),
		('fab fa-google-plus-g', 'Google+'),
		('fab fa-linkedin-in', 'LinkedIn'),
		('fab fa-instagram', 'Instagram'),
		('fab fa-twitter', 'Twitter'),
		('fab fa-airplane', 'Telegram')
	)
	icon = models.CharField(max_length = 255,choices= SOCIAL_ICONS, verbose_name = 'Соц-сеть')
	link = models.CharField(max_length = 500, verbose_name = 'Ссылка')

	def __str__(self):
		return self.link

	class Meta:
		verbose_name = 'Социальная сеть'
		verbose_name_plural = 'Социальные сети'

class Features(models.Model):
	ICON_CHOISES = (
		('fas fa-trophy', 'Трофей'),
		('fas fa-desktop', 'Монитор'),
		('fas fa-book', 'Книжка'),
	)
	icon = models.CharField(max_length = 255,choices= ICON_CHOISES, verbose_name = 'Иконка')
	title_uz = models.CharField(max_length = 255, verbose_name = 'Заголовок [uz]')
	title_ru = models.CharField(max_length = 255, verbose_name = 'Заголовок [ru]')
	title_en = models.CharField(max_length = 255, verbose_name = 'Заголовок [en]')
	description_uz = models.TextField(verbose_name = 'Описание [uz]')
	description_ru = models.TextField(verbose_name = 'Описание [ru]')
	description_en = models.TextField(verbose_name = 'Описание [en]')

	def __str__(self):
		return self.title_ru
		
	class Meta:
		verbose_name = 'Преимущество'
		verbose_name_plural = 'Преимущества'