from main import ordenar_burbuja, procesar_sucursal


def test_ordenar_burbuja_ordena_por_sucursal():
    # Datos desordenados: cada fila es [sucursal, producto, ...]
    entrada = [
        ["003", "Pan", "", "", "2", "10"],
        ["001", "Leche", "", "", "1", "20"],
        ["002", "Queso", "", "", "3", "30"],
    ]
    resultado = ordenar_burbuja(entrada)

    # Esperamos que queden ordenadas por sucursal: 001, 002, 003
    sucursales = [fila[0] for fila in resultado]
    assert sucursales == ["001", "002", "003"]


def test_procesar_sucursal_calcula_resumen():
    filas = [
        ["001", "Pan",   "", "", "10", "5"],    # 10 x 5  = 50
        ["001", "Leche", "", "", "2",  "100"],  # 2 x 100 = 200
    ]
    resumen, indice_final = procesar_sucursal(filas, 0)

    assert resumen["sucursal"] == "001"
    assert resumen["unidades"] == 12              # 10 + 2
    assert resumen["mayor_producto"] == "Leche"   # 200 es el mayor
    assert resumen["menor_producto"] == "Pan"     # 50 es el menor
    assert indice_final == 2                       # procesó las 2 filas


def test_ordenar_burbuja_un_elemento():
    entrada = [["001", "Pan", "", "", "5", "10"]]
    resultado = ordenar_burbuja(entrada)
    assert resultado == [["001", "Pan", "", "", "5", "10"]]


def test_procesar_sucursal_un_solo_producto():
    filas = [
        ["005", "Agua", "", "", "8", "15"],
    ]
    resumen, indice_final = procesar_sucursal(filas, 0)
    assert resumen["unidades"] == 8
    assert resumen["mayor_producto"] == "Agua"
    assert resumen["menor_producto"] == "Agua"


def test_procesar_sucursal_acumula_mismo_producto():
    filas = [
        ["007", "Pan", "", "", "3", "10"],
        ["007", "Pan", "", "", "4", "10"],
    ]
    resumen, indice_final = procesar_sucursal(filas, 0)
    assert resumen["unidades"] == 7
    assert indice_final == 2