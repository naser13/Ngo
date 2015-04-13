from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from Ngo.forms import AddAdmin, AddExpert
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test


def user_home(request):
    pass

has_admin = False

# @user_passes_test(lambda u: u.is_superuser, login_url='login')
def add_admin(request):
    num = User.objects.count()
    if num == 0:
        if request.method == 'POST':
            has_admin = True
            form = AddAdmin(request.POST)
            form.save()
            return redirect('http://127.0.0.1:8000/')
        else:
            form = AddAdmin()
            return render(request, 'ali.html', {'form': form})
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')


@user_passes_test(lambda u: u.is_superuser, login_url='login')
def add_expert(request):
    if request.method == 'POST':
        form = AddExpert(request.POST)
        form.save()
    else:
        form = AddExpert()
    return render(request, 'ali.html', {'form': form})

