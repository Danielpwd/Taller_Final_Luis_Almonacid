from django import forms
from app_inscripcion.models import Inscripcion

class FormInscripcion(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = '__all__'
    
    fecha_inscripcion = forms.DateField(label="Fecha de inscripción", widget=forms.SelectDateWidget)
    hora_inscripcion = forms.TimeField(label="Hora de inscripción", widget=forms.TimeInput(attrs={'type':'time'}))
