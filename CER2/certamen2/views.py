from django.shortcuts import render
from .models import Entidad, Comunicado
# Create your views here.
def index(request):
    comunicados = Comunicado.objects.filter(visible = True)
    if request.method == 'POST':
        entidad_seleccionada = request.POST.get('select_entidad')
        if entidad_seleccionada:
            entidad = Entidad.objects.get(id = entidad_seleccionada)
            comunicados = Comunicado.objects.filter(visible = True).filter(entidad__nombre = entidad)     
    data = {
        "comunicados": comunicados,
        }
    return render(request,'certamen2/index.html',data)