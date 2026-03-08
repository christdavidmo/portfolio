from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_view, name='accueil'), # <-- Le chemin vide '' correspond à l'accueil
]