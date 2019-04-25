from django.contrib import admin
from django.contrib.auth.models import Group

from ciclistasapp.models import  Ciclista, Equipo, CiclistaEquipo, Prueba, PruebasEquipo
# Register your models here.

class CiclistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad', 'fecha_nacimiento')
    list_filter = ('nacionalidad', )



admin.site.unregister(Group)

admin.site.register(Ciclista, CiclistaAdmin)
admin.site.register(Equipo)
admin.site.register(CiclistaEquipo)
admin.site.register(Prueba)
admin.site.register(PruebasEquipo)
