import datetime
# Create your views here.

from django.shortcuts import render


def home_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']

    context = {
        'hora': agora.hour,
        'local': local,
        'topicos': topicos,
    }
    return render(request, 'portfolio/home.html', context)


def about_view(request):
    return render(request, 'portfolio/about.html')


def contact_view(request):
    return render(request, 'portfolio/contact.html')


def product_view(request):
    return render(request, 'portfolio/products.html')
