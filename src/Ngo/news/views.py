from django.shortcuts import render
from Ngo.forms import SignupForm


def home(request):
    return render(request, 'home.html')


#@login_required() for Experts
def edit(request):
    return render(request, 'new_article.html', )


def example(request):
    if request.method == 'POST':
        signup = SignupForm(request.POST)
    else:
        signup = SignupForm()
        return render(request, 'ali.html', {'form': signup})