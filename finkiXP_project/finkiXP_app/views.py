from django.shortcuts import render, redirect, get_object_or_404

from finkiXP_app.forms import TaskForm
from finkiXP_app.models import Subject, UserProfile, ExamTask


def index(request):
    return render(request, 'index.html')


def subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects.html', context={"subjects": subjects})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.uploaded_by = request.user
            task.save()
        else:
            print(form.errors)
        return redirect('index')

    form = TaskForm()
    return render(request, 'add_task.html', context={'form': form})


def subject_tasks(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    tasks = subject.tasks.all()
    return render(request, 'subject_tasks.html', {'subject': subject, 'tasks': tasks})


def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_tasks = ExamTask.objects.filter(uploaded_by=request.user)

    context = {
        'user_profile': user_profile,
        'user_tasks': user_tasks
    }
    return render(request, 'profile.html', context)
