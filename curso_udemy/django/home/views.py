from django.shortcuts import render

context = {
    'text': 'Texto diferente home.',
    'title': 'Texto exemplo title'
}

def home(request):
    print('home')
    return render(request,'home/index.html', context,)