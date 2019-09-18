from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
#from forms import Formulario

# Create your views here.
from rest_framework import viewsets
from rest_framework_mongoengine import viewsets as meviewsts
from .models import *
from .serializer import *
#import request


class AsambleistaViewSet(viewsets.ModelViewSet):
    queryset = Asambleista.objects.all()
    serializer_class = AsambleistaSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class LeyViewSet(viewsets.ModelViewSet):
    queryset = Ley.objects.all()
    serializer_class = Leyserializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class ComentarioLeyViewSet(viewsets.ModelViewSet):
    queryset = ComentarioLey.objects.all()
    serializer_class = ComentarioLeySerializer

class VotoViewSet(viewsets.ModelViewSet):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer

class lawsViewSet(meviewsts.ModelViewSet):
    lookup_field = 'id'
    queryset = laws.objects.all()
    serializer_class = lawsSerializer

# class contactomail(request):
# 	if request.method == 'POST':
# 		formulario=Formulario(request.POST)
# 		if formulario.is_valid():
# 			asunto= 'Este es un mensaje de GovernUS'
# 			mensaje = formulario.cleaned_data['mensaje']
# 			mail= EmailMessage(asunto, mensaje, to=['kmbmha@gmail.com'])
# 			mail.send()
# 		return HttpResponseRedirect('/')
# 	else:
# 		formulario=Formulario()

# 	return render_to_response('contactos.html',{'formulario':formulario}, context_instance=RequestContext(request))
