from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.

def home(request):
    return HttpResponse("<h1>HOME PAGE</h1><br><a href = 'posts'><h2>POSTS</h2></a>")

def post_list(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_details(request, id):
    post = get_object_or_404(Post, id = id)
    return render(request, 'blog/post_details.html', {'post':post})
