from django.shortcuts import render, HttpResponse

# Create your views here.


def opciones(request):

    return render(request, 'opciones.html')