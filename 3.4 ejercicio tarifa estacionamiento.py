print("Determinar cuanto debe cobrar por el uso del estacionamiento.")
horas = float(input("Ingrese el número de horas: "))

def calcular_tarifa(horas):
    if horas <= 2:
        return horas * 5.00
    elif horas <= 5:
        return 2 * 5.00 + (horas - 2) * 4.00
    elif horas <= 10:
        return 2 * 5.00 + 3 * 4.00 + (horas - 5) * 3.00
    else:
        return 2 * 5.00 + 3 * 4.00 + 5 * 3.00 + (horas - 10) * 2.00

tarifa = calcular_tarifa(horas)
print(f"La tarifa total es: ${tarifa:.2f}")
