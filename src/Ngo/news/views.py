from django.http import HttpResponse
from django.shortcuts import render, redirect
from Ngo.news.models import News, Answer
from Ngo.forms import SignupForm, AddPicForm, AddArticleForm
from random import randint
from django.contrib.auth.decorators import login_required, user_passes_test
from src.Ngo.persons.models import Admin


def home(request):
    i_news = News.get_all_important_news()
    r_news = News.get_all_regular_news()
    t_news = News.get_all_news()
    # date = datetime.now
    return render(request, 'home.html', {'i_news': i_news, 'r_news': r_news})

#
@login_required(login_url='login')
def create_article(request):
    # return HttpResponse(request.method)
    if request.method == 'POST':
        form2 = AddPicForm(request.POST, request.FILES)
        picForm =form2.save(commit=False)
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

        article.save()
        # form.save()
        print(request.POST['text'])
        return HttpResponse("done")

    form = AddArticleForm()
    form2 = AddPicForm()
    return render(request, 'new_article.html', {'form': form, 'form2':form2})


def example(request):
    if request.method == 'POST':
        signup = SignupForm(request.POST)
    else:
        signup = SignupForm()
        return render(request, 'ali.html', {'form': signup})


def edit(request):
    article = News.objects.get(id=1)
    return HttpResponse(article.text)
    # return render(request, 'show_new_news.html')


def show_article(request, id):
    news = News.objects.get(random_int=id)
    return render(request, 'Show_news.html', {'news': news})


@user_passes_test(lambda u: u.is_superuser, login_url='login')
def show_new_news(requst):
    n_news = News.get_all_new_news()
    return render(requst, 'show_new_news.html', {'n_news': n_news})


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
    return render(request,'edit_news.html', {'r_news': r_news, 'i_news': i_news})

@user_passes_test(lambda u: u.is_superuser, login_url='login')
def delete_news(request, id):
    News.objects.get(random_int=id).delete()
    return redirect('http://127.0.0.1:8000/editnews/')


def user_home(request):
    return redirect('http://127.0.0.1:8000/')