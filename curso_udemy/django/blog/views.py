from django.shortcuts import render

def exemplo(request):

    context = {
        'text': 'Olá exemplo.'
    }

    print('exemplo')
    return render(request, 'blog/exemplo.html', context)

def blog(request):

    context = {
        'text': 'Olá blog'
    }

    print('blog')
    return render(request, 'blog/index.html', context)

