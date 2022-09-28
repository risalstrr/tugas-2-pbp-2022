from re import T
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.models import Todolist

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data = Todolist.objects.filter(user=request.user)
    context = {
        'nama': request.user,
        'last_login': request.COOKIES['last_login'],
        'todolists': data
    }
    return render(request, "todolist.html", context)

def delete_todolist(request, id):
    todolist = Todolist.objects.get(pk=id)
    todolist.delete()
    return redirect('todolist:show_todolist')


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get("title")
        description = request.POST.get("description")
        create_new_task = Todolist(user=user, title=title, description=description)
        create_new_task.save()
        return redirect('todolist:show_todolist')

    return render(request, "create_new_task.html")

# if task is already finished
def finished(request, id):
    item = Todolist.objects.get(pk=id)
    item.is_finished = True
    item.save()
    return redirect('todolist:show_todolist')

# if task is not yet finished
def unfinished(request, id):
    item = Todolist.objects.get(pk=id)
    item.is_finished = False
    item.save()
    return redirect('todolist:show_todolist')