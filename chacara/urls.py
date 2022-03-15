from django.urls import path

from chacara.views import ChacaraListView

urlpatterns = [
    path('', ChacaraListView.as_view(), name='chacara-list'),
]
