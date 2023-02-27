from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *

menu = ['О сайте', 'Добавить статья', 'Обратная связь', 'Войти']
def index(request):
    posts = Songs.objects.all()
    return render(request, 'auen/index.html', {'posts': posts,  'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'auen/about.html', {'menu': menu, 'title': 'О сайте'})

def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Музыка по категориям.</h1><p>{catid}</p>")

def archive(request, year):
    if int(year)> 2022:
        #raise Http404()
        #return redirect('/', permanent = True)
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архив по годам.</h1><p>{year}</p>")

def  pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>404-Страница не найдена</h1>')

#def  pageForbidden(request, exception):
    #return HttpResponseForbidden('<h1>403-Страница запрещена</h1>')

#def  pageBadError(request, exception):
    #return HttpResponseBadError('<h1>400-Плохой запрос</h1>')

#def  pageServerError(request, exception):
    #return HttpResponseServerError('<h1>500-Внутренняя ошибка сервера</h1>')
# if(request.GET):
#         print(request.GET)
