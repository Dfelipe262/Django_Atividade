from django.contrib import admin
from .models import Postagem_Informatica, Postagem_Alimentos, Postagem_Apicultura

@admin.register(Postagem_Informatica)
class postagem_informatica_admin(admin.ModelAdmin):
    list_display=('titulo','texto','data_postagem','imagem')

@admin.register(Postagem_Alimentos)
class postagem_alimentos_admin(admin.ModelAdmin):
    list_display=('titulo','texto','data_postagem','imagem')

@admin.register(Postagem_Apicultura)
class postagem_apicultura_admin(admin.ModelAdmin):
    list_display=('titulo','texto','data_postagem','imagem')



# Register your models here.
