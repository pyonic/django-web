from django.shortcuts import render
import requests
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Banner, Contact, Phone, Email, Adress, About, Achievments, Blog, Socials, MainData, Features

def send_message(text):
	requests.get(f'https://api.telegram.org/bot5275430530:AAHOWgSCbBm3sQiSQs08SXpmNciw08N5WZo/sendMessage?chat_id=-1001402072595&text={text}')

def get_lang(request):
	lang = request.GET.get('l', default = False)

	if lang == False:
		try:
			lang = request.session['language']
		except:
			lang = 'ru'
	else:
		if lang != 'ru' and lang != 'en' and lang != 'uz':
			lang = 'ru'
	request.session['language'] = lang
	return lang

def set_user_language(request):
	lang = request.POST.get('lang', 'ru')
	request.session['language'] = lang

def get_context(request):
	banner = Banner.objects.all()
	about = About.objects.get()
	news = Blog.objects.filter(category = 'news', status = 'published').order_by('created_at')
	posts = Blog.objects.filter(category = 'blog', status = 'published').order_by('created_at')
	data = MainData.objects.get()
	features = Features.objects.all()

	context = {
		'banners' : banner,
		'about': about,
		'news': news,
		'posts': posts,
		'data': data,
		'features': features
	}
	context['socials'] = Socials.objects.all()
	context['phones'] = Phone.objects.all()
	context['address'] = Adress.objects.all()
	context['contact'] = Contact.objects.get()
	context['emails'] = Email.objects.all()
	context['lang'] = get_lang(request)
	return context

def index(request):
	if request.method == 'POST':
		phone = request.POST.get('phone')
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('message')
		msg = f'Новое сообщение от {name}\nНомер: {phone}\nПочта: {email}\nСообщение: {message}'
		send_message(msg)
	context = get_context(request)
	print(context['posts'])
	return render(request, 'main/index.html', context)

def handle_page_not_found(request, exception):
	context = get_context(request)
	return render(request, 'main/404.html', context)

def contacts(request):
	if request.method == 'POST':
		phone = request.POST.get('phone')
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('message')
		msg = f'Новое сообщение от {name}\nНомер: {phone}\nПочта: {email}\nСообщение: {message}'
		send_message(msg)

	context = get_context(request)
	return render(request, 'main/contact.html', context)

def about(request):
	about = About.objects.get()
	achievments = Achievments.objects.all()
	phone = Phone.objects.all()[0]
	lastest_blogs = Blog.objects.filter(category = 'blog', status = 'published').order_by('created_at')[:10]
	lang = get_lang(request)
	context = {
		'about': about,
		'achievments': achievments,
		'lang': lang,
		'phone': phone,
		'lastest_blogs': lastest_blogs
	}
	return render(request, 'main/about.html', context)

def posts(request, slug):
	post = Blog.objects.filter(slug = slug, status = 'published').first()
	lang = get_lang(request)
	if not post:
		return render(request, 'main/404.html')
	context = {
		'post': post,
		'lang': lang
	}
	return render(request, 'main/blog.html', context)

def post_list(request, category):
	page = request.GET.get('page', None)
	limit = request.GET.get('limit', None)
	if not page:
		page = 1
	if not limit:
		limit = 8
	context = get_context(request)
	
	if category != 'news' and category != 'blog':
		return render(request, 'main/404.html', context)

	search = request.GET.get('search', '')
	posts = Blog.objects.filter(Q(status='published'),Q(category=category), Q(title_uz__contains = search) | Q(title_ru__contains = search) | Q(title_en__contains = search) | Q(content_ru__contains = search) | Q(content_uz__contains = search) | Q(content_en__contains = search))
	post_paginate = Paginator(posts, limit).page(page)
	context['post_list'] = post_paginate
	context['posts'] = Blog.objects.filter(category = category, status = 'published').order_by('created_at')[:5]
	context['category'] = category
	context['num_pages'] = range(0,Paginator(posts, limit).num_pages)
	context['max_num'] = Paginator(posts, limit).num_pages

	return render(request, 'main/posts.html', context)