from django.contrib import admin
from .models import Criminal, Simulation, CrimeType, Memory  # Importa tus modelos aquí

# Registra los modelos
admin.site.register(Criminal)
admin.site.register(Simulation)
admin.site.register(CrimeType)
admin.site.register(Memory)
