from django.shortcuts import render, redirect
from .models import Inscripcion, Institucion
from .forms import FormInscripcion
from django.http import JsonResponse
from .serialiazers import InscripcionSerializer, InstitucionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.decorators import api_view

# Create your views here.
def index(request):
    return render(request, 'index.html')

def inscripcion(request):
    return render(request, 'inscripcion.html')

def listar_inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    data = {'inscripciones': inscripciones}
    return render(request, 'listar_inscripciones.html', data)

def agregar_inscripciones(request):
    form = FormInscripcion()
    if request.method == 'POST':
        print(request.POST)
        form = FormInscripcion(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregar_inscripciones.html', data)

def eliminar_inscripciones(request, id):
    inscripcion = Inscripcion.objects.get(id = id)
    inscripcion.delete()
    return redirect('/inscripcion/listar_inscripciones')

def actualizar_inscripciones(request, id):
    inscripcion_actualizada = Inscripcion.objects.get(id = id)
    form = FormInscripcion(instance=inscripcion_actualizada)
    if request.method == 'POST':
        form = FormInscripcion(request.POST, instance=inscripcion_actualizada)
        if form.is_valid() :
            form.save()
        return redirect('/inscripcion/listar_inscripciones')
    data = {'form' : form}
    return render(request, 'actualizar_inscripciones.html', data)

def verInscripcionDb(request):
    inscripcion = Inscripcion.objects.all()
    data = {'inscripcion' : list(inscripcion.values('nombre','telefono','fecha_inscripcion','institucion','hora_inscripcion','estado','observacion'))}

    return JsonResponse(data)


class ListarInscripcion(APIView):

    def get(self, request):
        inscri = Inscripcion.objects.all()
        serial = InscripcionSerializer(inscri, many=True)
        return Response(serial.data)

class DetalleInscripcion(APIView):

    def get_object(self, pk):
        try:
            return Inscripcion.objects.get(pk=pk)
        except Inscripcion.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        inscri = self.get_object(pk)
        serial = InscripcionSerializer(inscri)
        return Response(serial.data)
    
@api_view(['GET'])
def institucion_list(request):
    if request.method == 'GET':
        insti = Institucion.objects.all()
        serial = InstitucionSerializer(insti, many=True)
        return Response(serial.data)

@api_view(['GET'])
def institucion_detalle(request, pk):
    try:
        insti = Institucion.objects.get(id = pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSerializer(insti)
        return Response(serial.data)