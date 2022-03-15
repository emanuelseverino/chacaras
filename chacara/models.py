from django.contrib.auth.models import User
from django.db import models


class Chacara(models.Model):
    proprietario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='chacaras')
    nome = models.CharField(max_length=20)
    capacidade = models.CharField(max_length=5)
    descricao = models.TextField(max_length=1000)
    cep = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)

    def __str__(self):
        return self.nome
