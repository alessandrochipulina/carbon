from django.shortcuts import render
from .utils import estimate_footprint
from django.template import loader

# Create your views here.
from django.http import HttpResponse

def hola(request):
    return HttpResponse("¡Hola Django!")

def calcular_huella(request):
    resultado = None

    if request.method == 'POST':

        transporte = request.POST.get('transporte')
        pasajeros = int(request.POST.get('pasajeros', 1))
        distancia = float(request.POST.get('distancia', 0))
        energia = float(request.POST.get('energia', 0))
        gas = float(request.POST.get('gas', 0))
        combustible = request.POST.get('combustible')
        litros = float(request.POST.get('litros', 0))

        result = estimate_footprint(
            transporte,
            pasajeros,
            distancia,
            energia,
            gas,
            combustible,
            litros
        )

        context = {
                'result': result,                 
        }
    else:
        context = {'result': None}

    template = loader.get_template('form.html')
    return HttpResponse(template.render(context, request))