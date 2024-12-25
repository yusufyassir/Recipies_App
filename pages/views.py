from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class ListPost(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = "recipes"

class CreatePost(CreateView):
    model = Post
    fields = ['title', 'name', 'prep_time', 'ingredients', 'steps', 'img']
    template_name = 'add_recipe.html'
    success_url = reverse_lazy('home')

class DetailPost(DetailView):
    model = Post
    template_name = 'detailed_view.html'  # The template to render
    context_object_name = 'post'