from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from .forms import TaskForm
from .models import Tarea

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #   Agregar usuario
                usuario = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
                usuario.save()
                login(request, usuario)
                return redirect('tasks')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': "El usuario ya existe"
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': "Las contraseñas no coinciden"
        })

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        usuario = authenticate(request, username = request.POST['username'], password = request.POST['password'])

        if usuario is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': "El usuario ya existe"
            })
        else:
            login(request, usuario)
            return redirect('tasks')

@login_required
def tasks(request):
    tareas = Tarea.objects.filter(usuario=request.user).order_by('fecha_limite')
    return render(request, 'tasks.html', {
        'tareas': tareas
    })

@login_required
def tasks_finish(request):
    tareas = Tarea.objects.filter(usuario=request.user, hecho=True)
    return render(request, 'tasks.html', {
        'tareas': tareas
    })

@login_required
def tasks_search(request):
    if request.method == 'POST':
        tareas = Tarea.objects.filter(usuario=request.user, categoria__iexact=request.POST['search'])
        error = ""

        if not tareas:
            error = f"No se encontraron tareas relacionadas a: {request.POST['search']}"

        return render(request, 'pending_tasks.html', {
            'tareas': tareas,
            'error': error
        })

@login_required
def tasks_pending(request):
    tareas = Tarea.objects.filter(usuario=request.user, fecha_limite__isnull=True)

    return render(request, 'pending_tasks.html', {
        'tareas': tareas,
    })

@login_required
def tasks_create(request):
    if request.method == 'GET':
        return render(request, 'tasks_create.html', {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.usuario = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'tasks_create.html', {
                'form': TaskForm,
                'error': "Debe de agregar datos validos"
            })

@login_required
def tasks_edit(request, task_id):
    if request.method == 'GET':
        try:
            tarea = get_object_or_404(Tarea, pk=task_id, usuario=request.user)
            form = TaskForm(instance=tarea)
            return render(request, 'task_edit.html', {
                'form': form,
                'tarea': tarea
            })
        except:
            return redirect('tasks')
    else:
        try:
            tarea = get_object_or_404(Tarea, pk=task_id, usuario=request.user)
            form = TaskForm(request.POST, instance=tarea)
            form.save()
            return redirect('tasks')
        except:
            return redirect('tasks')

@login_required
def task_complete(request, task_id):
    tarea = get_object_or_404(Tarea, pk=task_id, usuario=request.user)
    if request.method == 'POST':
        tarea.fecha_limite = timezone.now()
        tarea.hecho = True
        tarea.save()
        return redirect('tasks')

@login_required
def task_delete(request, task_id):
    tarea = get_object_or_404(Tarea, pk=task_id, usuario=request.user)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tasks')

def public_tasks(request):
    tareas = Tarea.objects.all()

    if request.user.is_authenticated:
        tareas = tareas.filter(public=True).exclude(usuario=request.user)
    else:
        tareas = tareas.filter(public=True)

    return render(request, 'public_tasks.html', {
        'tareas_anonimas': tareas
    })