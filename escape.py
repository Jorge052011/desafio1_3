# se define math como m
import math as m

# Velocidad de escape

## ingreso de variables

Radio = int(input("Ingrese el radio de la tierra en Km: "))
Constante_g =float(input("ingrese la constante de gravedad en m/s: "))


Vel_escape = m.sqrt(2 * Radio * 1000 * Constante_g)

print(f"El valor de la velocidad de escape es de {Vel_escape:.1f} (m/s)")