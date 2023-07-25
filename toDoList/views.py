# import generic as generic
from django.shortcuts import render
from django.views import generic
from .models import Task


# Create your views here.
class IndexView(generic.ListView):
    context_object_name = "tasks"
    template_name = "toDoList/index.html"

    def get_queryset(self):
        return Task.objects.all()
