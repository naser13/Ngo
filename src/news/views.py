from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

#@login_required() for Experts
def edit(request):
    return render(request, 'new_article.html')