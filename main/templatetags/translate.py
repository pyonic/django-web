from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()
translations = {
    "contacts": {
        "what_uz": "Contactlar",
        "what_ru": "Контакты",
        "what_en": "Contacts",
        "contact_btn_uz": "Bog`lanish",
        "contact_btn_ru": "Связяться с нами",
        "contact_btn_en": "Contuct Us",
        "address_uz": "Manzil",
        "address_ru": "Адресс",
        "address_en": "Address",
        "email_uz": "Pochta",
        "email_ru": "Почта",
        "email_en": "Email",
        "phone_uz": "Kontakt",
        "phone_ru": "Номер",
        "phone_en": "Phone",
        "title_uz": "Biz bilan bog`laning",
        "title_ru": "Напишите нам",
        "title_en": "Get In Touch",
        "button_uz": "Jonatish",
        "button_ru": "Отправить",
        "button_en": "Submit",
        "f_name_uz": "Ismingiz",
        "f_name_ru": "Ваше имя",
        "f_name_en": "Your name",   
        "f_email_uz": "Elektron manzilingiz",
        "f_email_ru": "Адресс электронной почты",
        "f_email_en": "Your email",
        "f_phone_uz": "Telefon raqamingiz",
        "f_phone_ru": "Номер телефона",
        "f_phone_en": "Phone number",
        "f_message_uz": "Murojatingiz...",
        "f_message_ru": "Ваше сообщение...",
        "f_message_en": "Your message",
        "subtitle_uz": "Soragani uyalmang",
        "subtitle_ru": "Не стесняйтесь спрашивать",
        "subtitle_en": "Don’t Hesitate To Ask",
        "contact_us_uz": "Biz bilan bog`laning va savolingizga javob oling",
        "contact_us_ru": "Свяжитесь с нами и получите ответы на свои вопросы",
        "contact_us_en": "Contuct us and get answers to your questions"
    },
    "about": {
        "title_uz" : "Biz haqimizda",
        "title_ru" : "О нас",
        "title_en" : "About",
        "detail_uz": "Biz haqimizda batafsil",
        "detail_ru": "Подробней о нас",
        "detail_en": "Details about us"
    },
    "blog": {
        "what_uz": "Blog",
        "what_ru": "Блог",
        "what_en": "Blog",
        "title_uz": "Ohirgi blog postlar",
        "title_ru": "Последние публикации",
        "title_en": "Latest blog post"
    },
    "news": {
        "what_uz": "Yangiliklar",
        "what_ru": "Новости",
        "what_en": "News",
        "title_uz": "Ohirgi yangiliklar",
        "title_ru": "Последние новости",
        "title_en": "Latest news"
    },
    "aside": {
        "search_uz": "Izlash",
        "search_ru": "Поиск",
        "search_en": "Search",
        "keywords_uz": "Kalit sozlar",
        "keywords_ru": "Ключевые фразы",
        "keywords_en": "Enter keywords",
        "category_uz": "Toifalar ro`yhati",
        "category_ru": "Список категорий",
        "category_en": "Category list",
        "recent_uz": "Oxirgi nashrlar",
        "recent_ru": "Последние публикации",
        "recent_en": "Recent posts"
    },
    "static": {
        "quick_links_uz": "Sahifalar",
        "quick_links_ru": "Быстрые ссылки",
        "quick_links_en": "Quick links",
        "home_uz": "Bosh sahifa",
        "home_ru": "Главная",
        "home_en": "Home"
    }
}
@register.simple_tag()
def translate(block,key, lang):
    try:
        k = key+"_"+lang
        return translations[block][k]
    except Exception as e:
        print(e)
        return 'undef'

register.filter('translate', translate)