import functools
import operator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import inlineformset_factory
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from rest_framework import generics
from abmsocios import forms
from abmsocios.models import Socio, Datos_Medicos, Telefono, Domicilio
from abmsocios.serializers import ListadoSocioSerializer


class BusquedaSocio(LoginRequiredMixin, generics.ListAPIView):
    """Filtrado de socios por parametros de busqueda //ENDPOINT."""

    serializer_class = ListadoSocioSerializer

    def get_queryset(self):
        busqueda = self.kwargs['keyword'] 
        try:
            busqueda = int(busqueda)
            
        except ValueError:
            pass

        if type(busqueda) is int:
            resultado = Socio.objects.filter(
                documento__icontains=busqueda
            )
        else:
            busqueda = busqueda.split()
            resultado = Socio.objects.filter(
                functools.reduce(operator.and_,
                                 (Q(nombre__icontains=b) for b in busqueda)) |
                functools.reduce(operator.and_,
                                 (Q(apellido__icontains=b) for b in busqueda))
            )        
        return resultado


class ListadoSociosView(LoginRequiredMixin, generic.ListView):
    """List of all the members in the database.

    """

    model = Socio
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(ListadoSociosView, self).get_context_data(**kwargs)
        socio_list = Socio.objects.all()
        paginator = Paginator(socio_list, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            socio_page = paginator.page(page)
        except PageNotAnInteger:
            socio_page = paginator.page(1)
        except EmptyPage:
            socio_page = paginator.page(paginator.num_pages)

        context['socio_list'] = socio_page
        return context


class SocioDetallesView(LoginRequiredMixin, generic.DetailView):
    """Member details form.

    Show's all data from the selected member.

    """

    model = Socio

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        socio = Socio.objects.get(pk=pk)
        context = super(SocioDetallesView, self).get_context_data(pk=pk)
        context['telefonos'] = socio.telefono_set.all()
        context['domicilios'] = socio.domicilio_set.all()
        try:
            context['datos_medicos'] = Datos_Medicos.objects.get(socio=pk)
        except ObjectDoesNotExist:
            print(socio.nombre_completo, ' no tiene datos medicos')

        return context


@login_required
def home(request):
    """Detalles estadisticos para dashboard."""
    num_socios = Socio.objects.all().count()
    num_socios_activos = Socio.objects.filter(estado=True).count()
    num_socios_inactivos = Socio.objects.filter(estado=False).count()

    return render(
        request,
        'home.html',
        context={
            'num_socios': num_socios,
            'num_socios_activos': num_socios_activos,
            'num_socios_inactivos': num_socios_inactivos
            }
    )


class CrearSocio(LoginRequiredMixin, FormView):
    """New member instance.

       Opens a new member form.

       If the form was correctly fill redirects to the member's details
       page, if not remains in the form page indicating the errors.

    """

    template_name = 'nuevo_socio.html'
    form_class = forms.SocioModelForm
    success_url = '/'

    def post(self, request):
        pk = request.POST.get('documento')
        form = forms.SocioModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('detalle-socio', pk=pk)
        else:
            print(form.errors)
            return render(request, 'nuevo_socio.html', {'form': form})


class EditarSocio(LoginRequiredMixin, FormView):
    """
    Obtencion y edicion de socio.

    Obtiene los detalles del socio selecionandolo por numero de documento.
    Incluye formulario de edicion para dichos datos.
    """

    template_name = 'editar_socio.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        socio = Socio.objects.get(pk=pk)
        socio_form = forms.SocioModelForm(instance=socio)
        telefonos_socio = forms.TelefonoFormSet(instance=socio)
        domicilios_socio = forms.DomicilioFormSet(instance=socio, prefix='domicilio')
        try:
            datosmedicos_socio = forms.DatosMedicosModelForm(
                instance=socio.datos_medicos
                )
        except ObjectDoesNotExist:
            datosmedicos_socio = forms.DatosMedicosModelForm()
        return render(request, 'editar_socio.html', {
                        'socio': socio_form,
                        'numero_socio': socio.numero_socio,
                        'nombre_completo': socio.nombre_completo,
                        'foto_perfil': socio.foto_perfil,
                        'telefono': telefonos_socio,
                        'domicilio': domicilios_socio,
                        'datos_medicos': datosmedicos_socio
                    })

    def post(self, request, *args, **kwargs):
        pk = request.POST.get('documento')
        socio = get_object_or_404(Socio, pk=pk)
        socio_form = forms.SocioModelForm(
                        request.POST,
                        request.FILES,
                        instance=socio
                    )
        # telefonos_form = forms.TelefonoFormSet(
        #                    request.POST,
        #                    instance=socio,
        #                    prefix='telefono'
        #                )
        domicilios_form = forms.DomicilioFormSet(
                            request.POST,
                            instance=socio,
                            prefix='domicilio'
                       ) 
        try:
            datos_medicos = socio.datos_medicos          
        except Datos_Medicos.DoesNotExist:
            datos_medicos = Datos_Medicos.objects.create(socio=socio)

        datosmedicos_form = forms.DatosMedicosModelForm(
                                    request.POST,
                                    instance=datos_medicos
                                )
      
        if socio_form.is_valid() and datosmedicos_form.is_valid() and domicilios_form.is_valid():# and telefonos_form.is_valid()  :
            
            socio_form.save()
        #    telefonos_form.save()
            domicilios_form.save()
            datosmedicos_form.save()
            return redirect('detalle-socio', pk=pk)
        
        #socio_form = forms.SocioModelForm(instance=socio)
        #    telefonos_form = forms.TelefonoFormSet(instance=socio, prefix='telefono')
        #domicilios_form = forms.DomicilioFormSet(instance=socio, prefix='domicilio')
        #datosmedicos_form = forms.DatosMedicosModelForm(instance=socio.datos_medicos)

        return render(request, 'editar_socio.html', {
                    'socio': socio_form,
            #        'telefono': telefonos_form,
                    'domicilio': domicilios_form,
                    'datos_medicos': datosmedicos_form
                    })


class Presentacion(TemplateView):

    template_name = "presentacion.html"
