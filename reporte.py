def ordenar_por_ingreso(resultados):
    """Lista de (codigo, datos) de mayor a menor ingreso."""
    return sorted(resultados.items(), key=lambda item: item[1]["ingreso"], reverse=True)


def calcular_ingreso_global(resultados):
    """Suma de los ingresos de todos los vuelos."""
    return sum(datos["ingreso"] for datos in resultados.values())


def imprimir_reporte(resultados):
    ordenados = ordenar_por_ingreso(resultados)
    linea = "-" * 78
    print("\nREPORTE DE VUELOS (ordenado por ingreso, de mayor a menor)")
    print(linea)
    print(f"{'Vuelo':<8}{'Pasaj.':>7}{'P. original':>13}{'P. final':>11}"
          f"{'Ingreso':>13}  {'Baja ocupación':<14}")
    print(linea)
    for codigo, d in ordenados:
        descuento = d["precio_final"] != d["precio_original"]
        p_final = f"{d['precio_final']:.2f}" if descuento else "sin desc."
        baja = "SÍ" if d["baja_ocupacion"] else "No"
        print(f"{codigo:<8}{d['pasajeros']:>7}{d['precio_original']:>13.2f}"
              f"{p_final:>11}{d['ingreso']:>13.2f}  {baja:<14}")
    print(linea)
    print(f"INGRESO TOTAL GLOBAL: {calcular_ingreso_global(resultados):,.2f}")