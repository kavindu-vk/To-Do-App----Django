from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from . models import *
from . forms import *

def index(request):
    todo = Todo.objects.all()
    return render(request, 'index.html', {'todo':todo})

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added the task.")
            return redirect('index')
        else:
            messages.warning(request, "There is an error!")
            return redirect('add-todo')
    else:
        form = TodoForm()       
    return render(request, 'add-todo.html', {'form':form})
    
def edit_todo(request, pk):
    todo = get_object_or_404(Todo ,pk=pk)
    if request.method == 'POST':
        form = EditTodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Update your task..")
            return redirect('index')
        else:
            messages.warning(request, "Something went wrong")
            return redirect('index')
    else:
        form = EditTodoForm(instance=todo)
    context = {'form':form, 'todo':todo}
    return render(request, 'edit-todo.html', context)

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('index')
    return render(request, 'delete-todo.html', {'todo':todo})

def complete_todo(request, pk):
    if request.method == 'POST' and request.is_ajax():
        todo = get_object_or_404(Todo, pk=pk)
        completed = request.POST.get('completed', False)
        todo.completed = completed
        todo.save()
        return JsonResponse({'message': 'Task completion status updated.'})
    else:
        return JsonResponse({'error': 'Invalid request.'}, status=400)

