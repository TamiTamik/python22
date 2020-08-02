from django.shortcuts import render
from django.http import HttpResponse
from . models import Post, Category
# Create your views here.
def index(request):
    category_list = Category.objects.all()
    context = {
        'categories': category_list
    }
    return render(request, 'index.html', context)
def post(request, id):
    print('category id --->', id)
    category_list = Category.objects.all()
    post_list = Post.objects.filter(category_id = id)
    context = {
        'categories': category_list,
        'posts': post_list
    }
    return render(request, 'post.html', context)
def comment(request):
    return render(request, 'comment.html')
def about(request):
    return render(request, 'about.html')