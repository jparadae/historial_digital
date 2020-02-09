from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from transversal.models import Cliente, Profesional, Paciente

# Create your models here.
class Cita(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)	
	#establecimiento = models.CharField(max_length=200)
	fecha_citacion = models.DateField()
	hora_citacion = models.TimeField()
	cupos = models.IntegerField(default=1)
	es_cancelada = models.BooleanField(default=False)
	usuario = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Agenda cargada por categoria"
		verbose_name_plural = "Agendas cargadas por Categorias"

	def __unicode__(self):
		return "#%s (Profesional: %s)" % (self.id, self.profesional.rut)

class Reserva(models.Model):
	cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
	es_cancelada = models.BooleanField(default=False)
	contact_campania = models.IntegerField(blank=True, null=True)
	contact_status = models.IntegerField(blank=True, null=True)
	usuario = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	recordatorio = models.BooleanField(default=False)

	class Meta:
		verbose_name = "Agenda Reservada"
		verbose_name_plural = "Agendas Reservadas"

	def __unicode__(self):
		return "#%s (Cita #%s)" % (self.id, self.cita.id)
