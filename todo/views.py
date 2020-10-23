from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if(request.method == 'POST'):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form':form }
    return render(request, 'todo/list.html', context)

def manageTask(request, pkey):
    task = Task.objects.get(id=pkey)
    form = TaskForm(instance = task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance = task)

        if(form.is_valid()):
            form.save()
            return redirect('/')

    context = { 'form' : form }
    return render(request, 'todo/manage_task.html',context)

def removeTask(request, pkey):
    task = Task.objects.get(id=pkey)

    if(request.method == 'POST'):
        task.delete()
        return redirect('/')


    context = {'item': task}
    return render(request, 'todo/delete.html', context)