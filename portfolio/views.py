import datetime
# Create your views here.

from django.shortcuts import render

from portfolio import models, forms


def home_page_view(request):
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


def project_view(request):
    data = datetime.datetime.today().year

    # Projects
    projects = models.Projects.objects.all()

    # TFC

    form = forms.TfcsForm(request.POST or None, request.FILES)

    if form.is_valid():
        form.save()

    form = forms.TfcsForm()
    tfcs = models.tfcs.objects.all()

    context = {
        'ano': data,
        'projects': projects,
        'tfcs': tfcs,
        'form': form,
    }
    return render(request, 'portfolio/Projects.html', context)


def blog_view(request):
    data = datetime.datetime.today().year

    form = forms.BlogForm(request.POST or None)

    if form.is_valid():
        form.save()

    form = forms.BlogForm()

    blog = models.BlogsAnswers.objects.all()
    context = {
        'ano': data,
        'blogs': blog,
        'form': form,
    }

    return render(request, 'portfolio/blog.html', context)


def pw_view(request):
    data = datetime.datetime.today().year
    Tech = models.Tech.objects.all()
    Labs = models.labs.objects.all()
    News = models.news.objects.all()

    HTML = models.Tech.objects.all().filter(name="HTML")
    CSS = models.Tech.objects.all().filter(name="CSS")
    Boostrap = models.Tech.objects.all().filter(name="Bootstrap")

    context = {
        'ano': data,
        'HTML': HTML,
        'CSS': CSS,
        'Bootstrap': Boostrap,

        'Tech': Tech,
        'Labs': Labs,
        'News': News
    }

    return render(request, 'portfolio/Web Programming.html', context)
