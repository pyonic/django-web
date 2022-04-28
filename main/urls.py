from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
	path('', views.index, name='index'),
	path('contacts/', views.contacts, name='contacts'),
	path('about/', views.about, name='about'),
	path('post/<slug:slug>', views.posts, name='posts'),
	path('posts/<str:category>', views.post_list, name='post_list')
]