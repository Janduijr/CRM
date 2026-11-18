from django.urls import path
from .views import Lista_produtos

urlpatterns = [
    path('listar/', Lista_produtos, name='listar_produtos'),
]
