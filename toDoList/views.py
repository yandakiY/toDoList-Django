# import generic as generic
from django.shortcuts import render ,HttpResponseRedirect ,get_object_or_404
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
        return Task.objects.all().filter(view=True).order_by('-date_creation')


class TaskDeletedView(generic.ListView):
    context_object_name = "tasks_deleted"
    template_name = "toDoList/task_deleted.html"
    
    def get_queryset(self):
        return Task.objects.all().filter(view=False)
    

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


# function delete new task
def deleteTask(request , task_id):
    # list of id Task , for Task True
    list_id_task = [task.id for task in Task.objects.all() if task.view]
    print(list_id_task)
    # get id of task
    # get item who correspond
    # change value of view
    
    # task_to_delete = get_object_or_404(Task , id=task_id)
    # print(task_to_delete)
    
    if (task_id in list_id_task):
        # get item task who correspond
        task_to_delete = get_object_or_404(Task , id=task_id)
        # change value of view
        task_to_delete.view = False
        # and now save that
        task_to_delete.save()
    else:
        # render Error 404
        return render(request , "toDoList/error404.html")
    
    # # try 
    # try:
    #     # change value of view
    #     task_to_delete.view = False
    #     # and now save that
    #     task_to_delete.save()
    # except (KeyError):
    #     return render(request , "toDoList/index.html" , {"error_message":"Operation impossible to perform"})
    
    
    return HttpResponseRedirect(reverse('toDoList:index' , args=()))
    # pass
    
def restoreTask(request , task_id):
    # get lists task deleted
    task_deleted = [task.id for task in Task.objects.all()]
    
    if (task_id in task_deleted):
        # get item
        task = get_object_or_404(Task , id=task_id)
        # change view
        task.view = True
        # save change
        task.save()
    else:
        # return Error 
        return render(request , "toDoList/error404.html")
    
    # redirection to Index
    return HttpResponseRedirect(reverse("toDoList:index" , args=()))