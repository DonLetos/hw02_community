from django.shortcuts import render
from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'about/author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Здесь можно произвести какие-то действия для создания контекста.
        # Для примера в словарь просто передаются две строки
        context['title'] = 'Об авторе проекта'
        context['text'] = ('На создание этой страницы '
                                'у меня ушло пять минут! Ай да я.')
        return context 
    
class AboutTechView(TemplateView):
    template_name = 'about/tech.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Здесь можно произвести какие-то действия для создания контекста.
        # Для примера в словарь просто передаются две строки
        context['title'] = 'Технологии'
        context['text'] = ('На создание этой страницы '
                                'у меня ушло 10 минут! Ай да я.')
        return context 