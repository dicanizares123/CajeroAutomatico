from django.urls import path
from .views import login_view, home_view, logout_view
from .views import eliminar_usuario
from .views import seleccionar_cuenta, cuentas_corriente, cuentas_ahorros, seleccionar_tarjeta, mostrar_saldo, retirar_dinero, depositar_dinero
from .views import welcome_view


urlpatterns = [
    path("", welcome_view, name="welcome"),
    path("login/", login_view, name="login"),
    path('logout/', logout_view, name='logout'),
    path("home/", home_view, name="home"),
    path('eliminar_usuario/<int:user_id>/', eliminar_usuario, name='eliminar_usuario'),
    path('seleccionar_cuenta/', seleccionar_cuenta, name='seleccionar_cuenta'),
    path('cuentas_corriente/', cuentas_corriente, name='cuentas_corriente'),
    path('cuentas_ahorros/', cuentas_ahorros, name='cuentas_ahorros'),
    path('seleccionar_tarjeta/<int:tarjeta_id>/', seleccionar_tarjeta, name='seleccionar_tarjeta'),
    path('mostrar_saldo/<int:tarjeta_id>/', mostrar_saldo, name='mostrar_saldo'),
    path('retirar/<int:tarjeta_id>/', retirar_dinero, name='retirar_dinero'),
    path('depositar/<int:tarjeta_id>/', depositar_dinero, name='depositar_dinero'),
]
