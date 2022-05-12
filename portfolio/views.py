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
    LP2 = models.subjects("Linguagens da Programação 2", "2nd",
                          "1st Semester", 6, "3rd", lp2Topics, 4,
                          "Nuno Fachada", lp2Projects)

    content = {
        'LP2name': LP2.name,
        'LP2Topics': LP2.topics
    }

    return render(request, 'portfolio/about.html', content)


def contact_view(request):
    return render(request, 'portfolio/contact.html')


def product_view(request):
    return render(request, 'portfolio/products.html')
