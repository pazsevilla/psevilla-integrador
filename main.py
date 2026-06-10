import csv

def cargar_csv(path):
    """Lee el CSV y devuelve (cabecera, filas)."""
    with open(path, mode='r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        cabecera = next(lector)
        filas = list(lector)
    return cabecera, filas


def ordenar_burbuja(filas):
    n = len(filas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if filas[j][0] > filas[j + 1][0]:
                filas[j], filas[j + 1] = filas[j + 1], filas[j]
            elif filas[j][0] == filas[j + 1][0] and filas[j][1] > filas[j + 1][1]:
                filas[j], filas[j + 1] = filas[j + 1], filas[j]
    return filas


def procesar_sucursal(filas, inicio):
    """
    Procesa todas las filas de UNA sucursal a partir del índice 'inicio'.
    Devuelve un diccionario con el resumen y el índice donde terminó.
    """
    sucursal_act = filas[inicio][0]
    i = inicio
    n = len(filas)

    mayor_prod, mayor_imp = "", 0
    menor_prod, menor_imp = "", float('inf')
    total_unidades = 0

    while i < n and filas[i][0] == sucursal_act:
        producto_act = filas[i][1]
        tot_pesos = 0
        tot_uni = 0
        while i < n and filas[i][0] == sucursal_act and filas[i][1] == producto_act:
            tot_pesos += int(filas[i][4]) * float(filas[i][5])
            tot_uni += int(filas[i][4])
            i += 1

        if tot_pesos > mayor_imp:
            mayor_prod, mayor_imp = producto_act, tot_pesos
        if tot_pesos < menor_imp:
            menor_prod, menor_imp = producto_act, tot_pesos

        total_unidades += tot_uni

    resumen = {
        "sucursal": sucursal_act,
        "unidades": total_unidades,
        "mayor_producto": mayor_prod,
        "mayor_importe": mayor_imp,
        "menor_producto": menor_prod,
        "menor_importe": menor_imp,
    }
    return resumen, i


def procesar_todo(filas):
    """Recorre todas las sucursales y devuelve la lista de resúmenes + el total general."""
    i = 0
    n = len(filas)
    resumenes = []
    total_general = 0

    while i < n:
        resumen, i = procesar_sucursal(filas, i)
        resumenes.append(resumen)
        total_general += resumen["mayor_importe"] + resumen["menor_importe"]

    return resumenes, total_general


if __name__ == "__main__":
    path_archivo = input("Indique el path del csv: ")
    esta_ordenado = input("¿El archivo esta ordenado? (Y/N): ").upper()

    cabecera, filas = cargar_csv(path_archivo)

    if esta_ordenado == 'N':
        print("Ordenando archivo... por favor espere.")
        filas = ordenar_burbuja(filas)

    resumenes, total_general = procesar_todo(filas)

    for r in resumenes:
        print(f"\n--- RESUMEN {r['sucursal']} ---")
        print(f"Unidades Vendidas: {r['unidades']}")
        print(f"Mayor Producto: {r['mayor_producto']} (${r['mayor_importe']:.2f})")
        print(f"Menor Producto: {r['menor_producto']} (${r['menor_importe']:.2f})")
        print("----------------------------------------------")

    print(f"\nTOTAL DE SUCURSALES: {len(resumenes)}")
    print(f"TOTAL GENERAL: ${total_general:.2f}")

