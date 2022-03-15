from django.shortcuts import render
from django.views.generic import ListView, DetailView

from chacara.models import Chacara


class ChacaraListView(ListView):
    model = Chacara


class ChacaraDetailView(DetailView):
    model = Chacara
