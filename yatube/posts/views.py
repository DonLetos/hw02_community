from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Post
from .models import Group

FIRST_TEN_POST = settings.FIRST_TEN_POST

def index(request):
    posts = Post.objects.order_by()[:FIRST_TEN_POST]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'title': 'Последние обновления на сайте'
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by()[:FIRST_TEN_POST]
    context = {
        'group': group,
        'posts': posts,
        'title': 'Записи сообщества ' + str(group)
    }
    return render(request, 'posts/group_list.html', context)
