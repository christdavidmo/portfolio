from django.db import models

# Create your models here.


class Profil(models.Model):
    nom = models.CharField(max_length=100)
    titre = models.CharField(max_length=150)
    presentation = models.TextField()
    photo = models.ImageField(upload_to='profil/', blank=True, null=True)

    def __str__(self):
        return self.nom

class Experience(models.Model):
    poste = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=100)
    periode = models.CharField(max_length=100)
    description = models.TextField()

class Formation(models.Model):
    diplome = models.CharField(max_length=150)
    ecole = models.CharField(max_length=100)
    periode = models.CharField(max_length=100)

class Projet(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projets/', blank=True, null=True)

class Reseau(models.Model):
    nom = models.CharField(max_length=50) # ex: Gmail, LinkedIn
    # On remplace URLField par CharField et on supprime icone_class
    lien = models.CharField(max_length=255) 

    def __str__(self):
        return self.nom

class Langue(models.Model):
    nom = models.CharField(max_length=50) # Exemple : Français, Anglais
    niveau = models.CharField(max_length=50) # Exemple : Courant, Technique, Intermédiaire

    def __str__(self):
        return f"{self.nom} ({self.niveau})"
    
class Competence(models.Model):
    nom = models.CharField(max_length=100) # Exemples : Excel (TCD), Power BI, SQL...
    
    def __str__(self):
        return self.nom