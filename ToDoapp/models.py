from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )
    id = models.IntegerField(primary_key=True)
    task = models.CharField(max_length=500)
    deadline = models.DateField(blank=True, null=True)
    completed = models.BooleanField(blank=True, null=True, choices=TRUE_FALSE_CHOICES)
    def __str__(self):
        return self.task