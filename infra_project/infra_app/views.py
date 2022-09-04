"""View module function style base."""

from django.http import HttpResponse


def index(request):
    """Главная страница сайта."""
    return HttpResponse('У меня получилось!')


def second_page(request):
    """Страница с дополнительной информацией."""
    return HttpResponse('А это вторая страница')
