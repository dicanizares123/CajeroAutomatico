from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .models import CuentaBancaria, Tarjeta, Perfil 
from django.contrib.auth.models import User
from .forms import CustomAuthenticationForm

def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def eliminar_usuario(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('home')
    return render(request, 'eliminar_usuario.html', {'user': user})

@login_required
def home_view(request):
    user = request.user
    perfil = Perfil.objects.get(user=user)
    cuentas = CuentaBancaria.objects.filter(user=user)
    context = {
        'username': user.username,
        'cedula': perfil.cedula,
        'cuentas': cuentas,
    }
    return render(request, 'home.html', context)

@login_required
def seleccionar_cuenta(request):
    if request.method == 'POST':
        cuenta_id = request.POST.get('cuenta_id')
        cuenta = CuentaBancaria.objects.get(id=cuenta_id)
        request.session['cuenta_id'] = cuenta.id
        return redirect('home')
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login') 

@login_required
def seleccionar_cuenta(request):
    if request.method == 'POST':
        tipo_cuenta = request.POST.get('tipo_cuenta')
        if tipo_cuenta == 'corriente':
            return redirect('cuentas_corriente')
        elif tipo_cuenta == 'ahorros':
            return redirect('cuentas_ahorros')
    return redirect('home') 

@login_required
def cuentas_corriente(request):
    user = request.user
    cuentas = CuentaBancaria.objects.filter(user=user, tipo_cuenta='corriente')
    return render(request, 'cuentas_corriente.html', {'cuentas': cuentas}) 

@login_required
def cuentas_ahorros(request):
    user = request.user
    cuentas = CuentaBancaria.objects.filter(user=user, tipo_cuenta='ahorros')
    return render(request, 'cuentas_ahorros.html', {'cuentas': cuentas}) 

@login_required
def seleccionar_tarjeta(request, tarjeta_id):
    tarjeta = Tarjeta.objects.get(id=tarjeta_id)
    if request.method == 'POST':
        pin = request.POST.get('pin')
        if tarjeta.pin == pin:
            return render(request, 'mostrar_saldo.html', {'tarjeta': tarjeta})
        else:
            return render(request, 'seleccionar_tarjeta.html', {'tarjeta': tarjeta, 'error': 'PIN incorrecto'})
    return render(request, 'seleccionar_tarjeta.html', {'tarjeta': tarjeta})