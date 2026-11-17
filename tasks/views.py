
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task


# Display tasks, dashboard statistics and priority filtering
@login_required
def task_list(request):
    search_query = request.GET.get('search', '')
    priority_query = request.GET.get('priority', '')

    all_tasks = Task.objects.filter(user=request.user)

    # Dashboard statistics
    total_tasks = all_tasks.count()
    completed_tasks = all_tasks.filter(completed=True).count()
    pending_tasks = all_tasks.filter(completed=False).count()

    # Search and priority filtering
    tasks = all_tasks

    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    if priority_query:
        tasks = tasks.filter(priority=priority_query)

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'search_query': search_query,
        'priority_query': priority_query,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks
    })


# Add a new task
@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date') or None
        priority = request.POST.get('priority', 'Medium')

        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            due_date=due_date,
            priority=priority
        )

    return redirect('task_list')


# Mark task as completed
@login_required
def complete_task(request, task_id):
    task = get_object_or_404(
        Task, id=task_id, user=request.user
    )

    task.completed = True
    task.save()

    return redirect('task_list')


# Delete a task
@login_required
def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(
            Task, id=task_id, user=request.user
        )
        task.delete()

    return redirect('task_list')


# Edit an existing task
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(
        Task, id=task_id, user=request.user
    )

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date') or None
        task.priority = request.POST.get('priority', 'Medium')
        task.save()

        return redirect('task_list')

    return render(request, 'tasks/edit_task.html', {
        'task': task
    })
