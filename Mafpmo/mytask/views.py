from django.shortcuts import render, redirect
from .models import SelfTask
from .forms import SelfTaskForm
from django.views.generic import DetailView, UpdateView, DeleteView


def mytask_home(request):
    task = SelfTask.objects.all()
    return render(request, "mytask/new_task.html", {'task':task})


class TaskDetailView(DetailView):
    model = SelfTask
    template_name = 'mytask/details_view.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = SelfTask
    template_name = 'mytask/create.html'

    form_class = SelfTaskForm


class TaskDeleteView(DeleteView):
    model = SelfTask
    success_url = '/mytask'
    template_name = 'mytask/task-delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = SelfTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Задача не сохранена'

    form = SelfTaskForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'mytask/create.html', data)