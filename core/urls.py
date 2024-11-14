from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('criminal/<int:criminal_id>/create_simulation/', views.create_simulation, name='create_simulation'),
    path('simulation/create/', views.create_simulation_without_criminal, name='create_simulation_without_criminal'),  # Nueva ruta para crear simulación sin criminal_id,
    path('criminal/create/', views.create_criminal, name='create_criminal'),  # Nueva ruta para crear criminales
]
