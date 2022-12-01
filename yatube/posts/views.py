from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def index(request):
    template = 'posts/index.html'
    title = 'Социальная сеть блогеров Yatube'
    context = {
        'title': title,
        'text': 'Это главная страница проекта Yatube'
    }
    return render(request, template, context)


def group_posts(request, pk):
    return HttpResponse(f'Пост номер {pk}')

    """
       template = 'posts/group_list.html'
    context = {
        'text': 'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, template, context) 
    """