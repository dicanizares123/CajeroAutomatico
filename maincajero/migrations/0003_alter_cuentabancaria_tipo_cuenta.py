# Generated by Django 5.1.5 on 2025-01-30 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maincajero', '0002_transaccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentabancaria',
            name='tipo_cuenta',
            field=models.CharField(choices=[('corriente', 'Corriente'), ('ahorros', 'Ahorros')], max_length=10),
        ),
    ]
