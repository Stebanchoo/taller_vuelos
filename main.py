"""Programa principal: gestión de vuelos de una aerolínea."""

from datos import VUELOS, validar_vuelos
from ocupacion import procesar_vuelos
from reporte import imprimir_reporte


def main():
    validar_vuelos(VUELOS)
    resultados = procesar_vuelos(VUELOS)
    imprimir_reporte(resultados)


if __name__ == "__main__":
    main()