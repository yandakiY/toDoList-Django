from django.test import TestCase
from .models import Task
from django.utils import timezone
from django.urls import reverse
import datetime

# Create your tests here.
def create_task(task_text , duration=0, valueView=True):
    
    return Task.objects.create(task_text=task_text , date_creation=timezone.now()+datetime.timedelta(days=duration) , view=valueView)


class TestTaskModel(TestCase):
    
    
    # the task is more than a day old
    def testTaskIsMoreThanOneDayRecent(self):
        
        time = timezone.now() + datetime.timedelta(days=1 , seconds=1)
        task = Task(task_text="task not recent" , date_creation=time)
        self.assertIs(task.is_recent() , False)
        
    # the task is between now and yesterday at the same datetime
    def testTaskIsMoreThanOneDayRecent(self):
        time = timezone.now() - datetime.timedelta(hours=23 , minutes=59 , seconds=59)
        task = Task(task_text="task recent" , date_creation=time)
        self.assertIs(task.is_recent() , True)
        
    # Not Test for Date in future, because this future is not implemented

class TestIndexView(TestCase):
    # view only Task with view True
    def testViewTaskTrue(self):
        
        task_true = create_task(task_text="task true" ,duration=0)
        # calls index
        response = self.client.get(reverse('toDoList:index'))
        # compare
        self.assertQuerysetEqual(response.context['tasks'] , [task_true])
        
    
    # view more than 1 Task with view True
    def testViewMultipleTaskTrue(self):
        # task with view True
        task_true = create_task(task_text="task true" ,duration=0)
        # task 1 with view True
        task_true1 = create_task(task_text="task true 1" ,duration=0)
        # calls index
        response = self.client.get(reverse('toDoList:index'))
        # compare
        self.assertQuerysetEqual(response.context['tasks'] , [task_true, task_true1])

    # view only Task with view true, when we have a task true and a task false
    def testViewTaskTrueAndTaskFalse(self):
        # Task with view true
        task_true = create_task(task_text="task_true" , duration=0)
        # Task with view false
        create_task(task_text="Task false" , duration=0, valueView=False)
        # calls index
        response = self.client.get(reverse('toDoList:index'))
        # compare
        self.assertQuerysetEqual(response.context['tasks'] , [task_true])
        
    # we have only Tasks with view False
    def testViewTasksViewOnlyFalse(self):
        # task with view False
        task_false = create_task(task_text="task false" , duration=0, valueView=False)
        # new tasks with view False
        create_task(task_text="task false 1", duration=0, valueView=False)
        # calls index
        response = self.client.get(reverse('toDoList:index'))
        # compare
        self.assertEqual(len(response.context['tasks']) , 0)