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

class PruebaAdmin(admin.ModelAdmin):
    list_display = ( 'nombre_prueba', 'anio_edicion', 'etapas', 'total_km', 'ciclista_ganador')
    list_filter = ('anio_edicion', 'total_km',)

class CiclistaEquipoAdmin(admin.ModelAdmin):
    list_display = ('ciclista', 'equipo', 'fecha_inicio', 'fecha_fin')
    list_filter = ('ciclista', 'equipo',)

class PruebasEquipoAdmin(admin.ModelAdmin):
    list_display = ('prueba', 'equipo', 'puesto')
    list_filter = ('prueba', 'equipo', 'puesto',)




admin.site.unregister(Group)

admin.site.register(Ciclista, CiclistaAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(CiclistaEquipo, CiclistaEquipoAdmin)
admin.site.register(Prueba, PruebaAdmin)
admin.site.register(PruebasEquipo, PruebasEquipoAdmin)
