from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
