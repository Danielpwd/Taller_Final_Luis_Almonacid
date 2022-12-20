"""DJANGO_TALLER_FINAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_inscripcion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('inscripcion/', views.inscripcion),
    path('inscripcion/listar_inscripciones/', views.listar_inscripciones),
    path('inscripcion/agregar_inscripciones/', views.agregar_inscripciones),
    path('inscripcion/eliminar_inscripciones/<int:id>/', views.eliminar_inscripciones),
    path('inscripcion/actualizar_inscripciones/<int:id>/', views.actualizar_inscripciones),
    path('inscripcionDB/', views.verInscripcionDb),
    path('listaInscripcion/', views.ListarInscripcion.as_view()),
    path('listaInscripcion/<int:pk>', views.DetalleInscripcion.as_view()),
    path('listaInstitucion/', views.institucion_list),
    path('listaInstitucion/<int:pk>', views.institucion_detalle),
]
