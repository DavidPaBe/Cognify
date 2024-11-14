from django.db import models

# Modelo para el tipo de crimen
class CrimeType(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Asegura que cada tipo de crimen sea único
    description = models.TextField()

    def __str__(self):
        return self.name


# Modelo para el criminal
class Criminal(models.Model):
    name = models.CharField(max_length=100)
    crime_type = models.ForeignKey(CrimeType, on_delete=models.CASCADE)  # Relación con CrimeType
    sentence_length = models.PositiveIntegerField(help_text="Length of sentence in years")  # Solo valores positivos
    rehabilitation_option = models.BooleanField(default=False)  # True para rehabilitación acelerada

    def __str__(self):
        return self.name

    # Método adicional para verificar si el criminal tiene la opción de rehabilitación
    def can_be_rehabilitated(self):
        return self.rehabilitation_option


# Modelo para la memoria de un criminal
class Memory(models.Model):
    criminal = models.ForeignKey(Criminal, on_delete=models.CASCADE)  # Relación con Criminal
    memory_type = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"Memory for {self.criminal.name} - {self.memory_type}"

    # Puedes agregar métodos que simulen interacciones con la memoria, por ejemplo:
    def is_rehabilitative_memory(self):
        # Asegúrate de que sea un recuerdo relacionado con la rehabilitación
        return "rehabilitation" in self.memory_type.lower()


# Modelo para la simulación de la memoria de un criminal
class Simulation(models.Model):
    criminal = models.ForeignKey(Criminal, on_delete=models.CASCADE)  # Relación con Criminal
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE)  # Relación con Memory
    start_time = models.DateTimeField(auto_now_add=True)  # Timestamp para el inicio
    end_time = models.DateTimeField()  # Timestamp para el fin

    def __str__(self):
        return f"Simulation for {self.criminal.name} on {self.memory.memory_type}"

    # Método que simula la experiencia del recuerdo (puede ser extendido con lógica)
    def simulate(self):
        # Simulando alguna experiencia en la memoria del criminal, por ejemplo:
        duration = (self.end_time - self.start_time).seconds  # Duración de la simulación en segundos
        if duration < 60:
            return "Short simulation"
        elif duration < 3600:
            return "Medium simulation"
        else:
            return "Long simulation"
