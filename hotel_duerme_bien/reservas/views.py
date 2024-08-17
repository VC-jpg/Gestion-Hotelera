from django.shortcuts import render
from django.http import JsonResponse
from .forms import ReservaForm

def home(request):
    form = ReservaForm()
    return render(request, 'reservas/home.html', {'form': form})

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = {
                'status': 'success',
                'message': 'Tu reserva ha sido realizada con éxito.'
            }
        else:
            response_data = {
                'status': 'error',
                'message': 'Por favor, corrige los errores en el formulario.'
            }
    else:
        response_data = {
            'status': 'error',
            'message': 'Método no permitido.'
        }
    return JsonResponse(response_data)
