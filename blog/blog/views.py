from django.http import HttpResponse
#render
from django.shortcuts import render

def saludo(request):
    return render(request, "index.html")


def despedida(request):
    return HttpResponse("Buenas Noches!")


def nombre(request):
    return HttpResponse("Jordan" + " Nichiporuk")