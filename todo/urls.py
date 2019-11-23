from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='todo-index'),
    path('profile', views.profile, name='todo-profile'),
    path('signIn', views.signIn, name='signIn'),
    path('welcomePage', views.welcomePage, name='welcome')
]
