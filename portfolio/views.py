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

    LP2 = models.subjects("Programming Languages 2", "2nd",
                          "1st Semester", 6, "2020/2021", lp2Topics, 4,
                          "Nuno Fachada", lp2Projects)
    AI = models.subjects("Artificial Intelligence for Videogames", "2nd",
                         "2nd Semester", 6, "2020/2021", aiTopics, 5,
                         "Nuno Fachada", None)




    content = {
        # LP2
        'LP2name': LP2.name,
        'LP2Topics': LP2.topics,
        'LP2Projects': lp2Projects,
        'LP2etcs': LP2.etcs,
        'LP2semester': LP2.semester,
        'LP2lectiveYear': LP2.lective_year,

        # Ai
        'AITopics': aiTopics,
        'AIName': AI.name,
        'AIetcs': AI.etcs,
        'AISemester': AI.semester,
        'AIlectiveYear': AI.lective_year
        # Game Dev

    }

    return render(request, 'portfolio/about.html', content)


def contact_view(request):
    return render(request, 'portfolio/contact.html')


def product_view(request):
    return render(request, 'portfolio/products.html')
