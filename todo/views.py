from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm
from .models import UserInput




def index(request):
    return render(request, 'todo/index.html')


def profile(request):
    return HttpResponse('<h1>This is where your profile settings will exist</h1>')  

def signIn(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            #first_name = form.cleaned_data['first_name']
            #last_name = form.cleaned_data['last_name']
            #email = form.cleaned_data['email']

            return redirect('welcome')
        
          
    form=UserForm()
    return render(request, 'todo/form.html', {'form': form,})


def welcomePage(request):
    return render(request, 'todo/welcome.html')
          

