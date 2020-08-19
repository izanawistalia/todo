from django.shortcuts import render, redirect, get_object_or_404
from .models import task
from .forms import addForm, createUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from django.contrib.auth.models import User

# Create your views here.

def dash(request):
    return render(request, 'todo/dash.html')

def registerUser(request):
    form = UserCreationForm() #createUserForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/loginUser')
        else:
            messages.info(request, 'please follow the above given guidelines.')
    context = {'form': form}
    return render(request, 'todo/registerUser.html', context)

def loginUser(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #context = {'user': username}
            return redirect('/index')
        else:
            messages.info(request, 'username or password is incorrect!')

    context = {}
    return render(request, 'todo/loginUser.html', context)

@login_required
def logoutUser(request):
    logout(request)
    return redirect('/loginUser')

@login_required
def index(request):
    #print('wwwwwwwwwwwwwwwwwwwwwwwwwwwww'+str(request.user))
    user = request.user
    tasks = user.task_set.all()
    #tasks = task.objects.all()
    context = {'task': tasks, 'username': user}
    return render(request, 'todo/index.html', context)

@login_required
def add(request):
    #form = addForm(initial={'author': 'fluke'})
    #form = addForm()#form = task()
    if request.method == 'POST':
        #print('printing  ',request.POST)
        form = addForm(request.POST)
        #form.item = request.POST['task']
        #form.date_to_complete = request.POST['date']
        if form.is_valid():
            form.save()
            return redirect('/index')
        else:
            error = form.errors
            messages.info(request, error)
    #else{
    #form = addForm(initial={'author': request.user})
    form = addForm()
    context = {'form': form}
    return render(request, 'todo/add.html', context)
    #}

'''@login_required
def edit(request, pk):
    item = task.objects.get(id=pk)
    form = addForm(instance=item)
    if request.method == 'POST':
        form = addForm(request.POST, instance=item)
        print(form)
        if form.is_valid():
            print('edit mmmmmmm hhhhhhhhh   valid')
            form.save()
            return redirect('/index')
        else:
            print('edit mmmmmmm hhhhhhhhh   IINNNNNvalid')

    context = {'form': form}
    return render(request, 'todo/edit.html', context)'''

@login_required
def delete(request, pk):
    item = task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/index')

    context = {'item': item}
    return render(request, 'todo/delete.html', context)
    