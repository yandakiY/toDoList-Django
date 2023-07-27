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
    # get lists task deleted with view False
    task_deleted = [task.id for task in Task.objects.all() if task.view == False]
    
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


def removeDefinitelyTask(request , task_id):
    # get list of task with Task.view False
    task_to_delete_definitely = [task.id for task in Task.objects.all() if task.view == False]
    
    # check if task_id belongs is my list 
    if (task_id in task_to_delete_definitely):
        # get the object task which correspond
        task = get_object_or_404(Task , id=task_id)
        # delete this task
        task.delete()
        # redirect to 
        # pass
    else:
        return render(request , "toDoList/error404.html")

    return HttpResponseRedirect(reverse("toDoList:viewTaskDelete" , args=()))


def deleteAllTask(request):
    # delete all tasks with views equal to True
    lists_all_tasks = [task.id for task in Task.objects.all() if task.view == True]
    
    if len(lists_all_tasks) != 0:
        
        for task_id in lists_all_tasks:
            # get item , with the id in the lists
            t = get_object_or_404(Task , id=task_id)
            # change task.view to False
            t.view = False
            # save the change
            t.save()
    else:
        return HttpResponseRedirect(reverse("toDoList:index" , args=()))
    # return to Home page
    return HttpResponseRedirect(reverse("toDoList:index" , args=()))


def removeDefinitelyAllTask(request):
    # get all task with task.view = False
    lists_all_tasks_deleted = [task.id for task in Task.objects.all() if task.view == False]
        
    if len(lists_all_tasks_deleted) != 0:
        
        for task_id in lists_all_tasks_deleted:
            # get item , with the id in the lists
            t = get_object_or_404(Task , id=task_id)
            # delete this task
            t.delete()
    else:
        return HttpResponseRedirect(reverse("toDoList:viewTaskDelete" , args=()))
    # return to Home page
    return HttpResponseRedirect(reverse("toDoList:viewTaskDelete" , args=()))