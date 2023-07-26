from . import views
from django.urls import path

app_name = 'toDoList'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('addTask' , views.addTask , name="addTask")
]