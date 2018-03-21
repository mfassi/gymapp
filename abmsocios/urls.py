from django.conf import settings
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import static
from rest_framework.urlpatterns import format_suffix_patterns
from abmsocios import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^listadoSocios/$', views.ListadoSociosView.as_view(),
        name='listado-socios'),
    url(r'^socio/(?P<pk>\d+)', views.SocioDetallesView.as_view(),
        name='detalle-socio'),
    url(r'^presentacion/$', views.Presentacion.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

"""endpoints"""
urlpatterns += [
    url(r'^buscar/(?P<keyword>[A-Za-z0-9]+)', views.BusquedaSocio.as_view(),
        name='busqueda-socio-json'),
]

"""autenticacion"""
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

"""formularios de socios"""
urlpatterns += [
    url(r'^crearSocio/$', views.CrearSocio.as_view(), name='creacion-socio'),
    url(r'^editar/(?P<pk>\d+)', views.EditarSocio.as_view(),
        name='editar-socio'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
