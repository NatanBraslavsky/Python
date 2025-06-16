from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'text':'oi'
    }
    return render(request, 'index.html', context)

def blog(request):
    context = {
        'text':'blog'
    }
    return render(request, 'blog.html', context)