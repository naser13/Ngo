from django.shortcuts import render
from django.http import HttpResponse
from src.persons.models import Expert

def newsPage(request):
    return render(request, 'show_new_news.html')

def home(request):
    return render(request, 'home.html')

#@login_required() for Experts
def edit(request):
    return render(request, 'new_article.html')

def example(request):
    e = Expert()
    e.continent = 'al'
    e2 = Expert()
    e2.continent = 'af'
    experts = [e,e2]
    return render(request,'ali.html', {'Experts': experts})