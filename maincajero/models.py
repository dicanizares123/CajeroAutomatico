from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.user.username} - Cédula: {self.cedula}'

class CuentaBancaria(models.Model):
    TIPO_CUENTA_CHOICES = [
        ('corriente', 'Cuenta Corriente'),
        ('ahorros', 'Cuenta de Ahorros'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cuenta = models.CharField(max_length=20)
    tipo_cuenta = models.CharField(max_length=10, choices=TIPO_CUENTA_CHOICES)

    def __str__(self):
        return f'{self.user.username} - Cuenta: {self.cuenta}'

class Tarjeta(models.Model):
    cuenta_bancaria = models.ForeignKey(CuentaBancaria, on_delete=models.CASCADE, related_name='tarjetas')
    numero_tarjeta = models.CharField(max_length=20)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    pin = models.CharField(max_length=4)  # Campo PIN

    def __str__(self):
        return f'Tarjeta {self.numero_tarjeta} - Saldo: {self.saldo}' 

    def retirar(self, monto):
        if monto > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= monto
        self.save()

    def depositar(self, monto):
        self.saldo += monto
        self.save()
    

