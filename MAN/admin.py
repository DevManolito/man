from django.contrib import admin
from .models import Mascota

class mascotaAdmin(admin.ModelAdmin):

    list_display = ['codigo', 'nombre', 'edad', 'tipo', 'imagen']
    ordering = ['codigo']

admin.site.register(Mascota, mascotaAdmin)
