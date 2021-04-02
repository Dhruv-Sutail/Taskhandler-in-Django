
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse
from app.views import home,login,signup,addtodo,signout,delete_todo,change_todo

urlpatterns = [
    path('', home , name='home'),
    path('login', login , name='login'),
    path('signup/',signup),
    path('add-todo',addtodo),
    path('logout',signout),
    path('delete-todo/<int:id>',delete_todo),
    path('change-status/<int:id>/<str:status>',change_todo)
]
