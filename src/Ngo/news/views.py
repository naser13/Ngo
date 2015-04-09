from django.http import HttpResponse
from django.shortcuts import render
from Ngo.forms import SignupForm,AddPicForm


def home(request):
    return render(request, 'home.html')


#@login_required() for Experts
def create_article(request):
    if request.method == 'POST':
        # form = AddPicForm(request.POST, request.FILES)
        # form.save()
        return HttpResponse("done")
    form = AddPicForm()
    return render(request, 'new_article.html', {'form': form})


def example(request):
    if request.method == 'POST':
        signup = SignupForm(request.POST)
    else:
        signup = SignupForm()
        return render(request, 'ali.html', {'form': signup})