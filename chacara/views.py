from django.shortcuts import render
from django.views.generic import ListView

from chacara.models import Chacara


class ChacaraListView(ListView):
    model = Chacara
