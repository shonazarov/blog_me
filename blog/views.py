from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Blog
# Create your views here.

class BlogListView(ListView):
    model = Blog
    context_object_name = 'post_list'
    template_name = 'home.html'
    
class BlogDetail(DetailView):
    model = Blog
    template_name = 'post_detail.html'
    context_object_name = 'blog'
