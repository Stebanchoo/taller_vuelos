UMBRAL_DESCUENTO = 500
PORCENTAJE_DESCUENTO = 0.15


def calcular_precio_final(precio):
    """Aplica 15 % de descuento si el precio es mayor a 500."""
    if precio > UMBRAL_DESCUENTO:
        return precio * (1 - PORCENTAJE_DESCUENTO)
    return precio


def calcular_ingreso_vuelo(pasajeros, precio):
    """Ingreso total = pasajeros * precio final."""
    return pasajeros * calcular_precio_final(precio)