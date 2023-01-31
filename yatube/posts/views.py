from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Group


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'title': 'Последние обновления на сайте'
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'title': 'Записи сообщества ' + str(group)
    }
    return render(request, 'posts/group_list.html', context)


def group_list(request):
    templates = 'posts/group_list.html'
    return render(request, templates)
