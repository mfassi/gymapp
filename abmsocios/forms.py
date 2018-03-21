from django import forms
from django.contrib.auth.admin import User
from abmsocios.models import Socio, Datos_Medicos, ObraSocial, Telefono, Domicilio


class DatosMedicosModelForm(forms.ModelForm):
    obra_social = forms.ModelChoiceField(queryset=ObraSocial.objects.all(),
                                         required=False,
                                         widget=forms.Select(attrs={'class': 'ui fluid dropdown'}))

    class Meta:
        model = Datos_Medicos
        exclude = ['socio']
        widgets = {
            'osNumero_socio': forms.TextInput(attrs={'placeholder': 'Numero de Socio'}),
            'os_plan': forms.TextInput(attrs={'placeholder': 'Plan OS'}),
            'contacto_urgencia': forms.TextInput(attrs={'placeholder': 'Nombre Completo'}),
            'contacto_parentesco': forms.TextInput(attrs={'placeholder': 'Parentesco'}),
            'numero_urgencia': forms.TextInput(attrs={'placeholder': 'Telefono Contacto'}),
        }
        labels = {
            'os_plan': 'Plan',
            'osNumero_socio': 'Socio Numero',
            'numero_urgencia': 'Telefono'
        }


class SocioModelForm(forms.ModelForm):
    sexo = forms.ChoiceField(choices=Socio.sexo_opciones, widget=forms.Select(attrs={'class': 'ui dropdown', 'required': True}))

    class Meta:
        model = Socio
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombres', 'required': True}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellidos', 'required': True}),
            'documento': forms.TextInput(attrs={'placeholder': 'Nº de Documento', 'required': True}),
            'fecha_nacimiento': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa', 'required': True}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Email', 'required': True}),
            'fecha_apto': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}),
            'fecha_inscription': forms.DateInput(attrs={'required': True}),
        }
        labels = {
            'nombre': 'Nombres',
            'apellido': 'Apellidos',
            'correo': 'Email',
            'estado': 'Activar usuario?',
            'apto_fisico': 'Presento apto fisico?',
        }


class DomicilioModelForm(forms.ModelForm):
    tipo = forms.ChoiceField(choices=Domicilio.tipo_domicilio_opciones, required=False, widget=forms.Select(attrs={'class': 'ui fluid dropdown'}))

    class Meta:
        model = Domicilio
        exclude = ['socio']
        widgets = {
                    'calle': forms.TextInput(attrs={'placeholder': 'Calle', 'required': False}),
                    'numero': forms.TextInput(attrs={'placeholder': 'Numero', 'required': False}),
                    'piso': forms.TextInput(attrs={'placeholder': 'Piso', 'required': False}),
                    'departamento': forms.TextInput(attrs={'placeholder': 'Departamento', 'required': False}),
                    'barrio': forms.TextInput(attrs={'placeholder': 'Barrio', 'required': False}),
                    'localidad': forms.TextInput(attrs={'placeholder': 'Localidad', 'required': False}),
                    'codigo_postal': forms.TextInput(attrs={'placeholder': 'Codigo Postal', 'required': False}),
                    'provincia': forms.TextInput(attrs={'placeholder': 'Provincia', 'required': False}),
                    }


TelefonoFormSet = forms.inlineformset_factory(Socio, Telefono,
                    fields=('numero', 'tipo'),
                    extra=1,
                    widgets={
                        'tipo': forms.Select(attrs={'class': 'ui fluid dropdown'}),
                        'numero': forms.TextInput(attrs={'placeholder': 'Numero'}),
                    },
                    labels={
                        'numero': 'Numero'
                    },
                    max_num=3,
                    validate_max=True,
                    can_delete=True,
                    )

DomicilioFormSet = forms.inlineformset_factory(
                    Socio,
                    Domicilio,
                    form=DomicilioModelForm,
                    extra=1,
                    max_num=2,
                    validate_max=True,
                    can_delete=True,
                    )
                   

