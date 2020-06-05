from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    id = models.IntegerField(primary_key=True)
    task = models.CharField(max_length=500)
    deadline = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.task