from django.contrib import admin
from app_inscripcion.models import Inscripcion

# Register your models here.

class InscripcionAdmin(admin.ModelAdmin):
    list_display = ['nombre','telefono','fecha_inscripcion','institucion','hora_inscripcion','estado','observacion']

admin.site.register(Inscripcion, InscripcionAdmin)
