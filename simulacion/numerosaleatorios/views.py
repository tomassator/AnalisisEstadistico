from django.shortcuts import render, HttpResponse


# Create your views here.

def holamundo(request):
    return render(request, "holamundo.html")