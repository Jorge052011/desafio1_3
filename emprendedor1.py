#importando math para los calculos
import math as m

# Cálculo de utilidades

Precio_Suscripcion = float(input("ingrese precio de suscripción:"))
Usuarios_normales = int(input("ingrese número de usuarios normales : "))
Gastos = float(input("ingrese gastos: "))

Utilidades = Precio_Suscripcion * Usuarios_normales-Gastos

print(f"la utilidad es de {Utilidades:.2f} pesos en el período")