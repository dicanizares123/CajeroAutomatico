from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .models import CuentaBancaria, Tarjeta, Perfil 
from django.contrib.auth.models import User
from .forms import CustomAuthenticationForm
from decimal import Decimal
from django.shortcuts import get_object_or_404



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
    try:
        perfil = Perfil.objects.get(user=user)
    except Perfil.DoesNotExist:
        perfil = None  # Handle the case where the Perfil does not exist

    cuentas = CuentaBancaria.objects.filter(user=user)
    context = {
        'username': user.username,
        'cedula': perfil.cedula if perfil else 'N/A',  # Handle missing perfil
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

@login_required
def mostrar_saldo(request, tarjeta_id):
    tarjeta = Tarjeta.objects.get(id=tarjeta_id)
    return render(request, 'mostrar_saldo.html', {'tarjeta': tarjeta}) 

@login_required
def retirar_dinero(request, tarjeta_id):
    tarjeta = Tarjeta.objects.get(id=tarjeta_id)
    if request.method == 'POST':
        monto = float(request.POST['monto'])
        if monto > tarjeta.saldo:
            return render(request, 'mostrar_saldo.html', {'tarjeta': tarjeta, 'error': 'Saldo insuficiente'})
        tarjeta.retirar(monto)
        return redirect('mostrar_saldo', tarjeta_id=tarjeta.id)
    return redirect('home') 

def depositar_dinero(request, tarjeta_id):
    tarjeta = get_object_or_404(Tarjeta, id=tarjeta_id)
    if request.method == 'POST':
        monto = float(request.POST.get('monto'))

        tarjeta.depositar(monto)
        return redirect('mostrar_saldo', tarjeta_id=tarjeta.id)
    return render(request, 'depositar_dinero.html', {'tarjeta': tarjeta})

def retirar_dinero(request, tarjeta_id):
    tarjeta = get_object_or_404(Tarjeta, id=tarjeta_id)
    if request.method == 'POST':
        monto = float(request.POST.get('monto'))
        try:
            tarjeta.retirar(monto)
        except ValueError as e:
            # Manejar el error de saldo insuficiente
            return render(request, 'retirar_dinero.html', {'tarjeta': tarjeta, 'error': str(e)})
        return redirect('mostrar_saldo', tarjeta_id=tarjeta.id)
    return render(request, 'retirar_dinero.html', {'tarjeta': tarjeta}) 

def welcome_view(request):
    return render(request, 'welcome.html')