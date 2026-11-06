from django.shortcuts import render, redirect
from .models import Mascota

def home(request):
    return render(request, "MAN/home.html")

def mostrarMascotas(request):

    mascotas = Mascota.objects.all()

    data = {
        'mascotas': mascotas
    }

    return render(request, "MAN/mascotas.html", data)

def agregarMascota(request):

    if request.method == 'POST':

        nombre = request.POST.get("nombre")
        edad = int(request.POST.get("edad"))
        tipo = request.POST.get("tipo")
        imagen = request.POST.get("imagen")

        Mascota.objects.create(

            nombre = nombre,
            edad = edad,
            tipo = tipo,
            imagen = imagen
        )
        return redirect('')
        
    return redirect('mascotas')
    
