from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Task(models.Model):
    task_text = models.CharField(max_length=200)
    date_creation = models.DateTimeField("Date creation")
    view = models.BooleanField(default=True)
    
    def is_recent(self):
        time = timezone.now()
        return time - datetime.timedelta(days=1) <= self.date_creation <= time
        
    def __str__(self) -> str:
        return self.task_text
