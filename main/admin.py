from django.contrib import admin
from .models import Banner, Blog, Phone, Email, Contact, Adress, About, Achievments,Socials, MainData,Features

admin.site.register(Banner)
admin.site.register(Phone)
admin.site.register(Email)
admin.site.register(Adress)
admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Achievments)
admin.site.register(Socials)
admin.site.register(Features)

@admin.register(MainData)
class MainDataAdmin(admin.ModelAdmin):
	def has_delete_permission(self, request, obj=None):
		return False

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title_ru','slug','publish')
	list_filter = ('publish',)
	search_fields = ('title_ru','content_ru')
	prepopulated_fields = {'slug':('title_ru',)} #Автоматически создает ЧПУ (friendly urls)