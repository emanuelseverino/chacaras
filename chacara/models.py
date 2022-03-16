from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from datetime import datetime
from tinymce import models as tinymce_models

class Chacara(models.Model):

    estado_choice = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    )

    recursos_choices = (
        ('Acesso para Cadeirantes', 'Acesso para Cadeirantes'),
        ('Aquecedor', 'Aquecedor'),
        ('Ar condicionado no Salão', 'Ar condicionado no Salão'),
        ('Area para Camping', 'Area para Camping'),
        ('Area verde', 'Area verde'),
        ('Banheiros Masculino e Feminino', 'Banheiros Masculino e Feminino'),
        ('Banheiro Unissex', 'Banheiro Unissex'),
        ('Cachoeira', 'Cachoeira'),
        ('Campo de Futebol', 'Campo de Futebol'),
        ('Cervejeira', 'Cervejeira'),
        ('Cozinha equipada', 'Cozinha equipada'),
        ('Churrasqueira', 'Churrasqueira'),
        ('Dormitórios', 'Dormitórios'),
        ('Dormitórios com Ar condicionado', 'Dormitórios com Ar condicionado'),
        ('Escorregador na piscina', 'Escorregador na piscina'),
        ('Estacionamento', 'Estacionamento'),
        ('Freezer', 'Freezer'),
        ('Frente para Rio/Lago', 'Frente para Rio/Lago'),
        ('Localizado em Condominio', 'Localizado em Condominio'),
        ('Playground', 'Playground'),
        ('Piscina', 'Piscina'),
        ('Piscina Aquecida', 'Piscina Aquecida'),
        ('Piscina Coberta', 'Piscina Coberta'),
        ('Piscina Infantil', 'Piscina Infantil'),
        ('Pista de dança', 'Pista de dança'),
        ('Proibido animais', 'Proibido animais'),
        ('Proibido som Automotivo', 'Proibido som Automotivo'),
        ('Quadra de Areia', 'Quadra de Areia'),
        ('Quadra de Bocha', 'Quadra de Bocha'),
        ('Quadra de Tenis', 'Quadra de Tenis'),
        ('Rede de Volley na piscina', 'Rede de Volley na piscina'),
        ('Segurança', 'Segurança'),
        ('Sofás', 'Sofás'),
        ('Trilha Ecológica', 'Trilha Ecológica'),
        ('Vestiário', 'Vestiário'),
        ('Ventiladores', 'Ventiladores'),
    )

    tipo_eventos_choices = (
        ('Aniversário', 'Aniversário'),
        ('Casamentos', 'Casamentos'),
        ('Confraternização', 'Confraternização'),
        ('Festa Infantil', 'Aniversário Infantil'),
        ('Formatura', 'Formatura'),
        ('Outros', 'Outros'),
    )

    referencias_choices = (
        ('Açougue', 'Açougue'),
        ('Bar / Lanchonete', 'Bar / Lanchonete'),
        ('Distribuidora de Bebidas', 'Distribuidora de Bebidas'),
        ('Mercearia', 'Mercearia'),
        ('Padaria', 'Padaria'),
        ('Ponto de Onibus', 'Ponto de Onibus'),
        ('Supermercado', 'Supermercado'),
    )

    capacidade_choices = (
        ('Até 25 pessoas', 'Até 25 pessoas'),
        ('Até 50 pessoas', 'Até 50 pessoas'),
        ('Até 100 pessoas', 'Até 100 pessoas'),
        ('Até 150 pessoas', 'Até 150 pessoas'),
        ('Até 200 ou mais pessoas', 'Até 200 ou mais pessoas'),

    )

    pagamentos_choices = (
        ('Dinheiro', 'Dinheiro'),
        ('Cartão', 'Cartão'),
        ('Cartão Parcelado', 'Cartão Parcelado'),
        ('PIX', 'PIX'),
    )

    proprietario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='fotos/%Y/%m/%d/')
    imagem_1 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    imagem_2 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    imagem_3 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    imagem_4 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    imagem_5 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    imagem_6 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    imagem_7 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    imagem_8 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    nome = models.CharField(max_length=20)
    capacidade = models.CharField(choices = capacidade_choices, max_length=300, blank=True)
    espaco = models.IntegerField()                                          #em metros quadrados
    descricao = RichTextField()
    descricao_curta = tinymce_models.HTMLField(max_length=300)
    cep = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(choices = estado_choice, max_length=100)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    recursos = MultiSelectField(choices = recursos_choices, blank=True)
    outros_recursos = models.CharField(max_length=100, blank=True)
    is_featured = models.BooleanField(default=False)                           #é anuncio de destaque? (cliente paga mais)
    tipo_eventos = MultiSelectField(choices = tipo_eventos_choices, blank=True)
    pontos_referencia = MultiSelectField(choices = referencias_choices, blank=True)
    video_link = models.CharField(max_length=350)
    pagamentos = MultiSelectField(choices = pagamentos_choices, blank=True)
    telefone = models.IntegerField()
    whatsapp = models.IntegerField()
    instagram = models.CharField(max_length=300)
    facebook = models.CharField(max_length=300)
    data_add = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nome