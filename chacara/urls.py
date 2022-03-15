from django.urls import path

from chacara.views import ChacaraListView, ChacaraDetailView

urlpatterns = [
    path('', ChacaraListView.as_view(), name='chacara-list'),
    path('<int:pk>/', ChacaraDetailView.as_view(), name='chacara-detail'),
]
