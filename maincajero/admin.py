from django.contrib import admin
from .models import CuentaBancaria, Tarjeta, Perfil

# Register your models here.
admin.site.register(Perfil)

admin.site.register(CuentaBancaria)

admin.site.register(Tarjeta)