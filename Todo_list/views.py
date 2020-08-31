from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from . models import Todo

# Create your views here. 
"""class indexView(generic.ListView):
    todo_items = Todo.objects.all().order_by("added_date")
    template_name = 'Todo_list/index.html'
    
    def get_queryset(self):
        return """
def index(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'Todo_list/index.html', {"todo_items":todo_items})

@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    created_obj = Todo.objects.create(added_date=current_date, text=content)
    length_of_todo = Todo.objects.all().count()
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")