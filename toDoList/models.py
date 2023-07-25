from django.db import models


# Create your models here.
class Task(models.Model):
    task_text = models.CharField(max_length=200)
    date_creation = models.DateTimeField("Date creation")
    
    
    def __str__(self) -> str:
        return self.task_text
