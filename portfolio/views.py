import datetime
# Create your views here.

from django.shortcuts import render

from portfolio import models


def home_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']
    data = datetime.datetime.today().year

    context = {
        'ano': data
    }
    return render(request, 'portfolio/home.html', context)


def about_view(request):
    data = datetime.datetime.today().year

    # Subjects
    LP2 = models.Subject.objects.get(id=1)
    PW = models.Subject.objects.get(id=2)
    AI = models.Subject.objects.get(id=3)
    # suject_3 = models.Subject.objects.get(id=2)

    # Subject Topics
    lp2Topics = models.Topics.objects.all().filter(topicsSubject="LP2")
    aiTopics = models.Topics.objects.all().filter(topicsSubject="AI")
    pwTopics = models.Topics.objects.all().filter(topicsSubject="PW")

    # Programming Languages
    programmingLanguages = models.ProgrammingLanguages.objects.all()
    others = models.NonProgrammingLanguages.objects.all()

    # Description
    description = models.Description.objects.all()

    context = {
        # data
        'ano': data,
        # subjects
        'LP2': LP2,
        'AI': AI,
        'PW': PW,
        # Programing Languagens
        'Languages': programmingLanguages,
        'Others': others,
        # Topics
        'LP2Topics': lp2Topics,
        'AITopics': aiTopics,
        'PWTopics': pwTopics,
        # Projects

        # Description
        'Description': description,

    }

    return render(request, 'portfolio/about.html', context)


def contact_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    data = datetime.datetime.today().year

    context = {
        'hora': agora.now(),
        'local': local,
        'ano': data
    }

    return render(request, 'portfolio/contact.html', context)


def product_view(request):
    data = datetime.datetime.today().year

    # Projects
    beiramar = models.Projects.objects.all().filter(projectName="Beira-Mar!")
    loctans = models.Projects.objects.all().filter(projectName="Loctan's Adventure")
    redemption = models.Projects.objects.all().filter(projectName="Redemption: The Deadly Sin")

    context = {
        'ano': data,
        'beira-mar': beiramar,
        'loctans': loctans,
        'redemption': redemption,
    }
    return render(request, 'portfolio/products.html', context)


def blog_view(request):
    context = {

    }

    return render(request, 'portfolio/blog.html', context)


def pw_view(request):
    context = {

    }

    return render(request, 'portfolio/PW.html', context)
