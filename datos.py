VUELOS = {
    "AV101": {"pasajeros": 120, "precio": 450},
    "AV202": {"pasajeros": 45, "precio": 620},
    "AV303": {"pasajeros": 80, "precio": 500},
    "AV404": {"pasajeros": 30, "precio": 780},
    "AV505": {"pasajeros": 150, "precio": 300},
    "AV606": {"pasajeros": 49, "precio": 510},
}


def validar_vuelos(vuelos):
    """Valida que cada vuelo tenga pasajeros y precio válidos."""
    if not vuelos:
        raise ValueError("El diccionario de vuelos está vacío.")
    for codigo, info in vuelos.items():
        for campo in ("pasajeros", "precio"):
            if campo not in info:
                raise ValueError(f"Vuelo {codigo}: falta el campo '{campo}'.")
        if info["pasajeros"] < 0 or info["precio"] < 0:
            raise ValueError(f"Vuelo {codigo}: valores negativos no permitidos.")
    return True