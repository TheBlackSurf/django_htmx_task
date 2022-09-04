from django.shortcuts import render, HttpResponse
from .models import Task


def home(request):
    tasks = Task.objects.all().order_by('-created')
    context = {
        'tasks': tasks,
    }
    return render(request, 'core/home.html', context)


def add_task(request):
    title = request.POST.get('title')
    user = request.user
    if request.method == 'POST':
        if len(title) > 3:
            Task.objects.create(title=title, author=user)
    tasks = Task.objects.all().order_by('-created')
    return render(request, 'partials/task-list.html', {
        'tasks': tasks,
    })


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    tasks = Task.objects.all().order_by('-created')
    return render(request, 'partials/task-list.html', {
        'tasks': tasks,
    })



def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    tasks = Task.objects.all().order_by('-created')
    title = request.POST.get('title')
    if title:
        task.title = title
        task.save()
        return render(request, 'partials/task-list.html', {
            'tasks': tasks,
        })
    return render(request, 'partials/form.html', {
        'task': task,
    })


def check_title(request):
    title = request.POST.get('title')
    if len(title) < 4:
        return HttpResponse('<div style="color:red; ">Ten task jest zdecydowanie za krótki!</div>')
    else:
        return HttpResponse('')
