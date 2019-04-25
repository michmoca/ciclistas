from django.contrib import admin
from django.contrib.auth.models import Group

from ciclistasapp.models import  Ciclista, Equipo, CiclistaEquipo, Prueba, PruebasEquipo
# Register your models here.

class CiclistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad', 'fecha_nacimiento')
    list_filter = ('nacionalidad', )


class EquipoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'nacion', 'director')
    list_filter = ('nacion', )

class EquipoPrueba(admin.ModelAdmin):
    list_display = ( 'nombre_prueba', 'anio_edicion', 'etapas', 'total_km', 'ciclista_ganador')
    list_filter = ('anio_edicion', 'total_km',)


admin.site.unregister(Group)

admin.site.register(Ciclista, CiclistaAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(CiclistaEquipo)
admin.site.register(Prueba, EquipoPrueba)
admin.site.register(PruebasEquipo)
