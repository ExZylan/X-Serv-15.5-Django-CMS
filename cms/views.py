from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from .models import Pages

def barra(request):
	lista = Pages.objects.all()
	salida = "<ul>"
	for page in lista:
		salida += '<li><a href="page/' + str(page.id) + '">' + page.name + '</a>'
	salida += "</ul>"
	#salida += formulario

	return HttpResponse(salida)

@csrf_exempt
def pages(request, numero):
	if request.method == "POST":
		g = Pages(name = request.POST['nombre'], page = request.POST['pagina'])
		g.save()
	try:
		page = Pages.objects.get(id=int(numero))
	except Pages.DoesNotExist:
		return HttpResponseNotFound('<h1>' + numero + ' not found.</h1>')
	return HttpResponse(page.name + " " + str(page.page))