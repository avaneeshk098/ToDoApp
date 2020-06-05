from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoItem
from datetime import datetime

# Create your views here.
def index(request):
    todoItems = ToDoItem.objects.order_by('deadline')
    if request.method == "POST":
        item = ToDoItem()
        task = request.POST.get("task")
        date_string = request.POST.get("datetimepicker1")
        date = datetime.strptime(date_string, "%m-%d-%Y").date()
        item.task = task
        item.deadline = date
        item.save()      
        return HttpResponseRedirect('/')
    return render(request, 'index.html', {'todoItems': todoItems})

