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
        complete = request.POST.get("completed")
        date = datetime.strptime(date_string, "%m-%d-%Y").date()
        item.task = task
        item.completed = complete
        item.deadline = date
        item.save()      
        return HttpResponseRedirect('/')
    return render(request, 'index.html', {'todoItems': todoItems})

def delete(request):
    if request.is_ajax:
        value = request.POST.get("id")
        ToDoItem.objects.get(pk=value).delete()
    return HttpResponse('/')

def complete(request):
    if request.is_ajax:
        value = request.POST.get("id")
        item = ToDoItem.objects.get(pk=value)
        item.completed = True
        item.save()
    return HttpResponse('/')