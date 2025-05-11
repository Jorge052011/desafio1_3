#importando math para los calculos
import math as m

# Cálculo de utilidades

Precio_Suscripcion = float(input("ingrese precio de suscripción:"))
Usuarios_normales = int(input("ingrese número de usuarios normales : "))

Gastos = float(input("ingrese gastos totales: "))
Utilidad_anterior = float(input("ingrese las utilidades del año anterior en pesos, para el cálculo de la razón este debe ser diferente de cero: "))

if Utilidad_anterior == 0:
    print("no se puede calcular la razón ya que ingresó el valor cero en la utilidades anteriores")

else:


    Utilidades_actuales = (Precio_Suscripcion * Usuarios_normales)-Gastos
    Razon = Utilidades_actuales / Utilidad_anterior

    print(f"La utilidad actual es de  {Utilidades_actuales:.2f} pesos y la razón entre la utilidad actual y la utilidad anterior es de {Razon:.2f}")