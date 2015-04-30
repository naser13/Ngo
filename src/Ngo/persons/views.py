from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from Ngo.forms import AddAdmin, AddExpert, Add_ngo
from django.contrib.auth.decorators import user_passes_test
from src.Ngo.persons.models import Admin


def user_home(request):
    pass


# @user_passes_test(lambda u: u.is_superuser, login_url='login')
def add_admin(request):
    num = Admin.objects.count()
    if num == 0:
        if request.method == 'POST':
            form = AddAdmin(request.POST)
            form.save()
            return redirect('http://127.0.0.1:8000/')
        else:
            form = AddAdmin()
            return render(request, 'ali.html', {'form': form})
    else:
        return HttpResponseNotFound('<h1>404 Page not found</h1>')


@user_passes_test(lambda u: u.is_superuser, login_url='login')
def add_expert(request):
    if request.method == 'POST':
        form = AddExpert(request.POST)
        form.save()
    else:
        form = AddExpert()
    return render(request, 'ali.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser, login_url='login')
def add_NGO(request):
    if request.method == 'POST':
        form = Add_ngo(request.POST)
        ngo = form.save(commit=False)
        ngo.Website = 'http://127.0.0.1:8000/ngo/'+ngo.latin_name
        ngo.save()
        return redirect('http://127.0.0.1:8000/')
    else:
        form = Add_ngo()
        return render(request, 'ali.html', {'form': form})

