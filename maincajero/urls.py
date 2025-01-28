from django.urls import path
from . import views 
from django.contrib.auth.views import LoginView, LogoutView
from .views import login_view, home_view, logout_view
from .views import eliminar_usuario
from .views import seleccionar_cuenta, cuentas_corriente, cuentas_ahorros, seleccionar_tarjeta



urlpatterns = [
    path("login/", login_view, name="login"),
    path('logout/', logout_view, name='logout'),
    path("", home_view, name="home"),
    path('eliminar_usuario/<int:user_id>/', eliminar_usuario, name='eliminar_usuario'),
    path('seleccionar_cuenta/', seleccionar_cuenta, name='seleccionar_cuenta'),
    path('cuentas_corriente/', cuentas_corriente, name='cuentas_corriente'),
    path('cuentas_ahorros/', cuentas_ahorros, name='cuentas_ahorros'),
    path('seleccionar_tarjeta/<int:tarjeta_id>/', seleccionar_tarjeta, name='seleccionar_tarjeta'),


]
