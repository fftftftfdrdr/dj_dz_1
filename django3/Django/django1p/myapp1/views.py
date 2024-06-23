from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def home_view(request):
    html = """
    <html>
    <head><title>Главная</title></head>
    <body>
    <h1>Добро пожаловать на мой первый сайт на Django!</h1>
    <p>Это главная страница.</p>
    </body>
    </html>
    """
    logger.info("Главная страница была посещена")
    return HttpResponse(html)

def about_view(request):
    html = """
    <html>
    <head><title>О себе</title></head>
    <body>
    <h1>Обо мне</h1>
    <p>Меня зовут Иван Слукин. Это мой первый сайт на Django.</p>
    </body>
    </html>
    """
    logger.info("Страница 'О себе' была посещена")
    return HttpResponse(html)