from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('criminal/<int:criminal_id>/create_simulation/', views.create_simulation, name='create_simulation'),
]
