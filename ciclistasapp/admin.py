from django.contrib import admin
from ciclistasapp.models import  Ciclista, Equipo, CiclistaEquipo, Prueba, PruebasEquipo
# Register your models here.


admin.site.register(Ciclista)
admin.site.register(Equipo)
admin.site.register(CiclistaEquipo)
admin.site.register(Prueba)
admin.site.register(PruebasEquipo)
