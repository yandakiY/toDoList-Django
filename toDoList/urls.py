from . import views
from django.urls import path

app_name = 'toDoList'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('addTask' , views.addTask , name="addTask"),
    path('<int:task_id>/deleteTask' , views.deleteTask , name="deleteTask"),
    path('<int:task_id>/restoreTask' , views.restoreTask , name="restoreTask"),
    path('viewTaskDelete' , views.TaskDeletedView.as_view() , name="viewTaskDelete"),
    path('<int:task_id>/removeDefinitelyTask' , views.removeDefinitelyTask , name="removeDefinitelyTask")
]