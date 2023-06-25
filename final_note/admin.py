from django.contrib import admin
from .models import Validacion, Mensaje

class ValidacionAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'nota_c1', 'nota_c2', 'nota_c3', 'clasificacion')

admin.site.register(Validacion, ValidacionAdmin)

class MensajeAdmin(admin.ModelAdmin):
    list_display = ('texto','clasificacion')
admin.site.register(Mensaje, MensajeAdmin)