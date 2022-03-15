from django.contrib.auth import get_user_model
from django.db import models

Usuario = get_user_model()


class Chacara(models.Model):
    proprietario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='chacara')
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
