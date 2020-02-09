"""historial_digital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from agenda import views as agenda_views, api as agenda_api
from django.conf.urls import url, include
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from rest_framework import routers
from transversal import views as transversal_views, api as transversal_api, api_issabele


router = routers.DefaultRouter()
router.register(r'agenda/citas', agenda_api.CitasViewSet)
router.register(r'agenda/reservas', agenda_api.ReservasViewSet)
router.register(r'transversal/tipo-cliente', transversal_api.TipoClienteViewSet)
router.register(r'transversal/clientes', transversal_api.ClienteViewSet)
router.register(r'transversal/tipo-profesionales', transversal_api.TipoProfesionalViewSet)
router.register(r'transversal/profesionales', transversal_api.ProfesionalViewSet)
router.register(r'transversal/pacientes', transversal_api.PacienteViewSet)


urlpatterns = [
   # path('admin/', admin.site.urls),

    path('admin/', admin.site.urls),

    url('^$', agenda_views.index, name='home'),
    url(r'^agenda/$', agenda_views.index, name='agenda'),
    url(r'^agenda/reservar/$', agenda_views.reservar_cita, name='reservar-cita'),

    url(r'^agenda/mis-citas/$', agenda_views.mis_citas, name='mis-citas'),

    url(r'^cargar/citas/$', agenda_views.cargar, name='cargar'),
    url(r'^gestionar/$', agenda_views.gestionar, name='gestionar'),
    url(r'^historial/$', agenda_views.historial, name='historial'),
    url(r'^export/xls/$', agenda_views.export_citas_xls, name='export_citas_xls'),

    # API REST
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/contactabilidad/create-campania/$', api_issabele.create_campania, name='api-contactabilidad-create-campania'),
    url(r'^api/contactabilidad/send-cita/$', api_issabele.send_cita, name='api-contactabilidad-send-cita'), 
    url(r'^api/contactabilidad/cancel-cita/$', api_issabele.cancel_cita, name='api-contactabilidad-cancel-cita'),

    # Python Social Auth URLs
	url('', include('social.apps.django_app.urls', namespace='social')),

    # Login URL
	url(r'^accounts/', include('django.contrib.auth.urls')),
	#url(r'^accounts/changed_password/?$', auth.views.password_change),
    #url(r'^logout/$', auth.views.logout, {'next_page': '/'}, name='logout'),

    #probar recordatorio
    url(r'^gestionar/recordatorioCitas/$', agenda_views.recordatorioCitas, name='recordatorioCitas'),
]
