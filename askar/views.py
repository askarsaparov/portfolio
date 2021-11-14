from django.shortcuts import render

from askar.models import Home, About, Portfolio, Category, Skills, Profile, Cantact

def index(request):
    #Home
    home = Home.objects.latest('updated')

    #About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    #Skills
    categories = Category.objects.all()

    #Portfolio
    portfolios = Portfolio.objects.all()

    if request.method == "POST":
        contact = Cantact()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.message = request.POST.get('message')
        contact.save()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
    }

    return render(request, 'index.html', context)