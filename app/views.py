from django.shortcuts import render,redirect
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login as loginUser,logout
from app.forms import TODOForm
from app.models import TODO
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'login')
def home(request):
    form = TODOForm()
    if request.user.is_authenticated:
        user = request.user
        todos = TODO.objects.filter(user = user).order_by('priority')
        return render(request, 'index.html',context = {'form':form,'todos':todos})
    

def login(request):
    if request.method=="GET":
        form = AuthenticationForm()
        context ={
                "form":form
            }
        return render(request,'login.html',context=context) 
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                loginUser(request,user)
                return redirect('home')

        else:
            context ={
                "form":form
            }
            return render(request,'login.html',context=context) 


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context ={
            "form":form
        }
        return render(request,'signup.html',context=context)
    else:
        form = UserCreationForm(request.POST)
        context ={
            "form":form
        }
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
        else:
            return render(request,'signup.html',context=context)
            return HttpResponse("Form is InValid")


def addtodo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('home')
        else:
            return render(request, 'index.html',context = {'form':form})

def signout(request):
    logout(request)
    return redirect('login')

def delete_todo(request,id):
    TODO.objects.get(pk=id).delete()
    return redirect('home')

def change_todo(request,id,status):
    todo = TODO.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('home')
