from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.user.username} - Cédula: {self.cedula}'

class CuentaBancaria(models.Model):
    TIPO_CUENTA_CHOICES = [
        ('corriente', 'Corriente'),
        ('ahorros', 'Ahorros'),
    ]
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    cuenta = models.CharField(max_length=20)
    tipo_cuenta = models.CharField(max_length=10, choices=TIPO_CUENTA_CHOICES)

    def __str__(self):
        return f'{self.user.username} - Cuenta: {self.cuenta}'

class Tarjeta(models.Model):
    cuenta_bancaria = models.ForeignKey(CuentaBancaria, on_delete=models.CASCADE, related_name='tarjetas')
    numero_tarjeta = models.CharField(max_length=20)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    pin = models.CharField(max_length=4)  # Campo PIN

    @property
    def primeros_digitos(self):
        return self.numero_tarjeta[:4]
    
    def __str__(self):
        return f'Tarjeta {self.numero_tarjeta} - Saldo: {self.saldo}' 

    def retirar(self, monto):
        if monto > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= Decimal(monto)
        self.save()
        Transaccion.objects.create(tarjeta=self, tipo='retiro', monto=monto)

    def depositar(self, monto):
        self.saldo += Decimal(monto)
        self.save()
        Transaccion.objects.create(tarjeta=self, tipo='deposito', monto=monto)

class Transaccion(models.Model):
    TIPO_TRANSACCION_CHOICES = [
        ('deposito', 'Depósito'),
        ('retiro', 'Retiro'),
    ]

    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE, related_name='transacciones')
    tipo = models.CharField(max_length=10, choices=TIPO_TRANSACCION_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.get_tipo_display()} de {self.monto} en {self.tarjeta.numero_tarjeta} el {self.fecha}'
    

