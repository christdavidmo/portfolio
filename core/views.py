from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Profil, Experience, Formation, Projet, Reseau ,Langue,Competence

def portfolio_view(request):
    profil = Profil.objects.first() 
    context = {
        'profil': profil,
        'experiences': Experience.objects.all(),
        'formations': Formation.objects.all(),
        'projets': Projet.objects.all(),
        'reseaux': Reseau.objects.all(),
        'langues': Langue.objects.all(),
        'competences': Competence.objects.all(),
    }
    return render(request, 'core/index.html', context)