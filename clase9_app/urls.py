from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_objetos, name='lista_objetos'),
    path('crear/', views.crear_objeto, name='crear_objeto'),
]