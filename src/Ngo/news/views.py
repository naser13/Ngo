from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Ngo.news.models import News, Answer
from Ngo.forms import SignupForm, AddPicForm, AddArticleForm
from random import randint
from django.contrib.auth.decorators import login_required, user_passes_test
from Ngo.templatetags.date import Output
from src.Ngo.persons.models import Admin, Expert


def home(request):
    i_news = News.get_all_important_news()
    r_news = News.get_all_regular_news()
    expert = Admin.objects.get(username='admin')
    print(expert.id)
    return HttpResponse(expert.id)
    return render(request, 'home.html', {'i_news': i_news, 'r_news': r_news})

#


@login_required(login_url='login')
def create_article(request):
    # return HttpResponse(request.method)
    if request.method == 'POST':
        form2 = AddPicForm(request.POST, request.FILES)
        picForm = form2.save(commit=False)
        pic = picForm.pic
        integer = randint(0, 10000000)
        pic.name = str(integer)+'.jpg'
        form2.save()
        form = AddArticleForm(request.POST, request.FILES)
        article = form.save(commit=False)
        article.title_image.name = pic
        article.random_int = integer
        article.title = request.POST['title']
        article.description = request.POST['description']
        article.text = request.POST['text']
        user = request.user
        print(user.id)
        expert = Expert.objects.get(id=4)
        # print(len(expert))
        # article.continent = expert.ngo.continent
        article.save()
        # form.save()
        print(request.POST['text'])
        return HttpResponse("done")

    form = AddArticleForm()
    form2 = AddPicForm()
    return render(request, 'new_article.html', {'form': form, 'form2': form2})


def edit(request):
    article = News.objects.get(id=1)
    return HttpResponse(article.text)
    # return render(request, 'show_new_news.html')


def show_article(request, id):
    news = News.objects.get(random_int=id)
    date = persian_date(news)
    return render(request, 'Show_news.html', {'news': news, 'date': date})


@user_passes_test(lambda u: u.is_superuser, login_url='login')
def show_new_news(request):
    n_news = News.get_all_new_news()
    return render(request, 'show_new_news.html', {'n_news': n_news})


@user_passes_test(lambda u: u.is_superuser, login_url='login')
def update_news(request, id, status):
    news = News.objects.get(random_int=id)
    if status != 'd':
        news.status = status
        news.save()
    else:
        news.delete()
    return show_new_news(request)


@user_passes_test(lambda u: u.is_superuser, login_url='login')
def show_news(request):
    r_news = News.get_all_regular_news()
    i_news = News.get_all_important_news()
    return render(request, 'edit_news.html', {'r_news': r_news, 'i_news': i_news})


@user_passes_test(lambda u: u.is_superuser, login_url='login')
def delete_news(request, id):
    News.objects.get(random_int=id).delete()
    return redirect('http://127.0.0.1:8000/editnews/')


def user_home(request):
    return redirect('http://127.0.0.1:8000/')


def filter_news(request, continent):
    news = News.objects.filter(continent=continent)
    return render(request, 'show_new_news.html', {'n_news': news})


def show_NGO(request, name):
    return render(request, 'ngo/germany.html', {'page_title': name})


def persian_date(news):
    day = news.date.day
    month = news.date.month
    year = news.date.year
    date = datetime(year, month, day)

    today = datetime(2015, 3, 21)
    days = (date-today).days
    day = 1
    month = 1
    year = 1394

    while days > 0:
        day += 1
        if month <= 6 and day == 32:
            day = 1
            month += 1

        if 6 < month < 12 and day == 31:
            day = 1
            month += 1

        if day == 30 and month == 12:
            if year % 1391 == 0:
                day += 1
            else:
                day = 1
                month = 1
                year += 1

        if day == 31 and month == 12 and year % 1391 ==0:
            day = 1
            month = 1
            year += 1

        days -= 1
    mounths = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
    weekdays = ['دوشنبه', 'سه شنبه', 'چهار شنبه', 'پنج شنبه', 'جمعه', 'شنبه', 'یکشنبه']

    date3 = datetime(year, month, day)
    return str(date3.day)+' - '+mounths[date3.month-1]+' - '+str(date3.year)+' '