from django import forms
from .models import Criminal, Simulation

class CriminalForm(forms.ModelForm):
    class Meta:
        model = Criminal
        fields = ['name', 'crime_type', 'sentence_length', 'rehabilitation_option']
        widgets = {
            'sentence_length': forms.NumberInput(attrs={'min': 1, 'placeholder': 'Enter sentence length in years'}),
            'rehabilitation_option': forms.CheckboxInput(attrs={'class': 'checkbox-style'}),  # Personaliza el checkbox si es necesario
        }

    # Validación personalizada para sentence_length
    def clean_sentence_length(self):
        sentence_length = self.cleaned_data['sentence_length']
        if sentence_length <= 0:
            raise forms.ValidationError("The sentence length must be greater than zero.")
        return sentence_length

    # Puedes agregar otras validaciones personalizadas si es necesario
    def clean(self):
        cleaned_data = super().clean()
        crime_type = cleaned_data.get("crime_type")
        rehabilitation_option = cleaned_data.get("rehabilitation_option")

        # Ejemplo de validación para rehabilitación
        if rehabilitation_option and crime_type and crime_type.name in ['Felony', 'Murder']:
            raise forms.ValidationError("Rehabilitation option is not available for felonies or murder.")
        
        return cleaned_data

class SimulationForm(forms.ModelForm):
    class Meta:
        model = Simulation
        fields = ['criminal', 'memory', 'end_time']
