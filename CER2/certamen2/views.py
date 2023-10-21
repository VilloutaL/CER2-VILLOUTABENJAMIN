from django.shortcuts import render
from .models import Entidad, Comunicado

# Create your views here.
def index(request):
    return render(request,'certamen2/index.html')