from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profil, Experience, Formation, Projet, Reseau ,Langue ,Competence

admin.site.register(Profil)
admin.site.register(Experience)
admin.site.register(Formation)
admin.site.register(Projet)
admin.site.register(Reseau)
admin.site.register(Langue)
admin.site.register(Competence)