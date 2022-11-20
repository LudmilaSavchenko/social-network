from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Главная страница
def index(request):
    template = 'post/index.html'
    title = 'Социальная сеть Yatube'
    context = {
        'title': title,
        'text': 'Это главная страница проекта Yatube'
    }
    return render(request, template, context)

def group_posts(request):
    template = 'post/group_list.html'
    context = {
        'text': 'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, template, context)
