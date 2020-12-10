from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.


def index(request):
    project_list = Project.objects.all()
    context = {
        'project_list': project_list,
    }
    return render(request, 'projects/index.html', context)


def detail(request, project_id):
    project = Project.objects.get(pk=project_id)
    context = {
        'project': project
    }
    return render(request, 'projects/detail.html', context)


def create_project(request):
    form = ProjectForm(request.POST or None, request.FILES)

    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.created_by = request.user
        new_form.save()
        return redirect('projects:index')

    return render(request, 'projects/project-form.html', {'form': form})


def update_project(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(request.POST or None, request.FILES, instance=project)

    if form.is_valid():
        form.save()
        return redirect('projects:index')

    return render(request, 'projects/project-form.html', {'form': form, 'project': project})


def delete_project(request, id):
    project = Project.objects.get(id=id)

    if request.method == 'POST':
        project.delete()
        return redirect('projects:index')

    return render(request, 'projects/project-delete.html', {'project': project})
