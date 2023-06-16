from django.db import models

class Postagem_Informatica(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField()
    data_postagem = models.DateField()
    imagem = models.ImageField(upload_to='static/img')

    def __str__(self):
        return self.titulo
    

class Postagem_Alimentos(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField()
    data_postagem = models.DateField()
    imagem = models.ImageField(upload_to='static/img')

    def __str__(self):
        return self.titulo
    

class Postagem_Apicultura(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField()
    data_postagem = models.DateField()
    imagem = models.ImageField(upload_to='static/img')

    def __str__(self):
        return self.titulo

