#importando math para los calculos
import math as m

# Cálculo de utilidades

Precio_Suscripcion = float(input("ingrese precio de suscripción:"))
Usuarios_normales = int(input("ingrese número de usuarios normales : "))
Usuarios_premium = int(input("ingrese número de usuarios premium : "))
Gastos = float(input("ingrese gastos: "))

# Calculo de nuevas utiliddes con formula para normales y premium

Utilidades = (Precio_Suscripcion * Usuarios_normales+(Precio_Suscripcion*1.5*Usuarios_premium))-Gastos

print(f"la utilidad es de {Utilidades:.2f} pesos en el período")