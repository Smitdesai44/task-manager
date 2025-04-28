from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def create_task(request):
    if request.method == 'POST':
        form  = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')

    form = TaskForm()
    return render(request, 'create_task.html', {'form' : form})

def list_tasks(request):
    tasks = Task.objects.all().order_by('-due_date')
    return render(request, 'list_tasks.html', {'tasks' : tasks})

def detail_task(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'detail_task.html', {'task' : task})

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')

    form = TaskForm(instance=task)
    return render(request, 'update_task.html', {'form' : form})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('list_tasks')
    return render(request, 'delete_task.html', {'task' : task})    



