from django.shortcuts import render
from blog.data import posts

def exemplo(request):
    context = {
        'text': 'Olá exemplo.'
    }
    print('exemplo')
    return render(request, 'blog/exemplo.html', context)

def blog(request):
    context = {
        'posts': posts
    }
    print('blog')
    return render(request, 'blog/index.html', context)

def post(request, id):
    print('post', id)
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)
