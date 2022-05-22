import datetime
# Create your views here.

from django.shortcuts import render

from portfolio import models


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
    # Subjcts
    lp2Topics = ['SOLID', ' Design Patterns', 'Delegates', 'file Management',
                 'Threads', 'Events', 'Atributes']
    lp2Projects = ['https://github.com/malmaboy/wolf_and_sheepsLP2',
                   'https://github.com/JMatos1221/LP2_Recurso',
                   'https://github.com/malmaboy/NasaProject_LP2',
                   'https://github.com/malmaboy/wolf_and_sheepsLP2']

    aiTopics = ['Decicion Trees', 'Procedural Generation', 'Path Fiding',
                'Algorithm Family Minimax', 'Machine Learning']

    LP2 = models.Subject.objects.get(id=1)
    AI = models.Subject.objects.get(id=2)
    # suject_3 = models.Subject.objects.get(id=2)

    context = {
        'LP2': LP2,
        'AI': AI

    }

    return render(request, 'portfolio/about.html', context)


def contact_view(request):
    return render(request, 'portfolio/contact.html')


def product_view(request):
    return render(request, 'portfolio/products.html')
