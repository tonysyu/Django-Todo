from django.db import models
from django.utils import timezone
import datetime

class ThingsToDo(models.Model):
    todo_input=models.CharField(max_length=250)
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.todo_input

class UserInput(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name



