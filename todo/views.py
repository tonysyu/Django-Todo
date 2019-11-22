from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm


def index(request):
    return render(request, 'todo/index.html')


def profile(request):
    return HttpResponse('<h1>This is where your profile settings will exist</h1>')  

def signIn(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            print(form.cleaned_data)
    form=UserForm()
    return render(request, 'todo/form.html', {'form': form})
    #return HttpResponse('<h1>This will be the sign in Page for new users</h1>')      

