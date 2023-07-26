# import generic as generic
from django.shortcuts import render ,HttpResponseRedirect
from django.views import generic
from .models import Task
from django.utils import timezone
from .models import Task
from django.urls import reverse

# Create your views here.
class IndexView(generic.ListView):
    context_object_name = "tasks"
    template_name = "toDoList/index.html"

    def get_queryset(self):
        return Task.objects.all()


# function add new task in DB
def addTask(request):
    # get the task_text
    # get the datetime
    # field view is always True
    task_text = request.POST['task_text']
    date_creation = timezone.now()
    new_task = Task.objects.create(task_text=task_text , date_creation=date_creation)
    # save
    new_task.save()
    # redirection to index page
    return HttpResponseRedirect(reverse('toDoList:index' , args=()))