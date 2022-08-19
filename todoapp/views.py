from http.client import HTTPResponse
from re import template
from django.shortcuts import render
from django.views.generic import ListView , DetailView ,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

from todoapp.models import ToDoModel


# Create your views here.

class TodoList(ListView):
    template_name="list.html"
    model = ToDoModel

class TodoDetail(DetailView):
    template_name = "detail.html"
    model = ToDoModel

class TodoCreate(CreateView):
    template_name = "create.html"
    model = ToDoModel
    fields = ("title","memo","priority","duedate")
    success_url = reverse_lazy("list")
    # reverse...普通の反対の流れ。urlを反対回りにする
    
class TodoDelete(DeleteView):
    template_name = "delete.html"
    model = ToDoModel
    success_url = reverse_lazy("list")

class TodoUpdate(UpdateView):
    template_name = "update.html"
    model = ToDoModel
    fields = ("title","memo","priority","duedate")
    success_url = reverse_lazy("list")