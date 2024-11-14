from django.shortcuts import render, redirect,  get_object_or_404
from django.http import Http404
from .models import Criminal, Memory, Simulation
from .forms import SimulationForm, CriminalForm

def index(request):
    # Mostrar todos los criminales disponibles
    criminals = Criminal.objects.all()
    return render(request, 'core/index.html', {'criminals': criminals})


def create_criminal(request):
    if request.method == 'POST':
        form = CriminalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página principal o donde desees después de crear un criminal
    else:
        form = CriminalForm()
    return render(request, 'core/create_criminal.html', {'form': form})

def create_simulation(request, criminal_id):
    criminal = get_object_or_404(Criminal, id=criminal_id)
    
    if request.method == "POST":
        # Aquí podríamos usar un formulario para validar la entrada
        memory_type = request.POST.get('memory_type')
        description = request.POST.get('description')
        end_time = request.POST.get('end_time')

        if not memory_type or not description or not end_time:
            # Validación básica: Si alguno de los campos es vacío, muestra un mensaje de error
            return render(request, 'core/create_simulation.html', {'criminal': criminal, 'error': 'Todos los campos son obligatorios'})

        try:
            # Crear la memoria
            memory = Memory.objects.create(
                criminal=criminal,
                memory_type=memory_type,
                description=description
            )

            # Crear la simulación
            simulation = Simulation.objects.create(
                criminal=criminal,
                memory=memory,
                end_time=end_time  # Aquí podrías procesar `end_time` si necesitas convertirlo
            )

            return render(request, 'core/simulation_result.html', {'simulation': simulation})
        
        except Exception as e:
            # Manejo de excepciones en caso de errores al guardar la simulación
            return render(request, 'core/create_simulation.html', {'criminal': criminal, 'error': f'Error al crear la simulación: {str(e)}'})

    return render(request, 'core/create_simulation.html', {'criminal': criminal})

def create_simulation_without_criminal(request):
    if request.method == 'POST':
        form = SimulationForm(request.POST)
        if form.is_valid():
            simulation = form.save()
            return redirect('index')
    else:
        form = SimulationForm()
    return render(request, 'core/create_simulation.html', {'form': form})
