from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.contrib.auth import authenticate , login , logout
from .models import *
# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  
    context_object_name = 'posts' 
    ordering = ['-date_posted']  
    paginate_by = 10 

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def home(request):
    recent_posts = Post.objects.order_by('-date_posted')[:5]  
    return render(request, 'blog/home.html', {'recent_posts': recent_posts, })

def about(request):
    return render(request, 'blog/about.html')








