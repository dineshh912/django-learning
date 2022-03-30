from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.

class BlogPostView(ListView):
    model = Post
    template_name = "blog/home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class BlogAddView(CreateView):
    model = Post
    template_name = "blog/post_add_new.html"
    fields =["title", "body"]
    

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_edit.html"
    fields =["title", "body"]


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html",
    success_url = reverse_lazy("home")