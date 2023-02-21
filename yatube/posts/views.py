from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Post, User
from .models import Group
from users.forms import ContactForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

FIRST_TEN_POST = settings.FIRST_TEN_POST


def authorized_only(func):
    # Функция-обёртка в декораторе может быть названа как угодно
    def check_user(request, *args, **kwargs):
        if request.user.is_authenticated:
            # Возвращает view-функцию, если пользователь авторизован.
            return func(request, *args, **kwargs)
        # Если пользователь не авторизован — отправим его на страницу логина.
        return redirect('/auth/login/')
    return check_user


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, FIRST_TEN_POST)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': post_list,
        'title': 'Последние обновления на сайте',
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


@login_required
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)

    post_list = Post.objects.filter(group=group).all()
    paginator = Paginator(post_list, FIRST_TEN_POST)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'posts': post_list,
        'title': 'Записи сообщества ' + str(group),
        'page_obj': page_obj
    }
    return render(request, 'posts/group_list.html', context)


def user_contact(request):
    # Проверяем, получен POST-запрос или какой-то другой:
    if request.method == 'POST':
        # Создаём объект формы класса ContactForm
        # и передаём в него полученные данные
        form = ContactForm(request.POST)
        # Если все данные формы валидны - работаем с "очищенными данными" формы
        if form.is_valid():
            # Берём валидированные данные формы из словаря form.cleaned_data
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # subject = form.cleaned_data['subject']
            # message = form.cleaned_data['body']
            # При необходимости обрабатываем данные
            # ...
            # сохраняем объект в базу
            form.save()
            # Функция redirect перенаправляет пользователя
            # на другую страницу сайта, чтобы защититься
            # от повторного заполнения формы
            return redirect('/thank-you/')
        # Если условие if form.is_valid() ложно и данные не прошли валидацию -
        # передадим полученный объект в шаблон,
        # чтобы показать пользователю информацию об ошибке
        # Заодно заполним все поля формы данными, прошедшими валидацию,
        # чтобы не заставлять пользователя вносить их повторно
        return render(request, 'contact.html', {'form': form})
    # Если пришёл не POST-запрос - создаём и передаём в шаблон пустую форму
    # пусть пользователь напишет что-нибудь
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def profile(request, username):
    # Здесь код запроса к модели и создание словаря контекста
    user_t = get_object_or_404(User, username=username)
    users_posts = user_t.posts.all()
    paginator = Paginator(users_posts, FIRST_TEN_POST)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'user': user_t,
        'page_obj': page_obj,
        'count_post': paginator.count
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    # it_post = get_object_or_404(Post, pk=post_id)
    post = Post.objects.filter(id=post_id).all()
    first_30_simvols = 30
    one_post = post[0]
    text = one_post.text[:first_30_simvols]

    users_posts = one_post.author.posts.all()
    paginator = Paginator(users_posts, FIRST_TEN_POST)
    context = {
        'title': 'Пост ' + text,
        'first_30_simvols': first_30_simvols,
        'count_post': paginator.count,
        'post': one_post
    }
    return render(request, 'posts/post_detail.html', context)
