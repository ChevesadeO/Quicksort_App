# ============================================================
#  UNIVERSIDAD TECNOLÓGICA DE PANAMÁ
#  Centro Regional de Colón
#  Facultad de Ingeniería de Sistemas Computacionales
#
#  Asignatura : Estructura de Datos II
#  Laboratorio: #3 – Eficiencia Algorítmica y Ordenamiento
#  Facilitador: Ing. Ariel Martínez
#  Tema       : Implementación del algoritmo Quicksort
#  Lenguaje   : Python 3
# ============================================================

import random   # Para generar números aleatorios
import time     # Para medir el tiempo de ejecución


# ------------------------------------------------------------
# FUNCIÓN: generar_lista
# ------------------------------------------------------------
# Genera exactamente 20 números aleatorios en el rango [1, 100].
# Utiliza random.randint(a, b) que devuelve un entero N tal que
# a <= N <= b.
# ------------------------------------------------------------
def generar_lista(cantidad: int = 20, minimo: int = 1, maximo: int = 100) -> list:
    """Retorna una lista de 'cantidad' números aleatorios entre minimo y maximo."""
    lista = []
    for _ in range(cantidad):
        lista.append(random.randint(minimo, maximo))
    return lista


# ------------------------------------------------------------
# FUNCIÓN: particion
# ------------------------------------------------------------
# Núcleo del algoritmo Quicksort.
#
# El esquema utilizado es "Lomuto partition":
#   1. Se elige el ÚLTIMO elemento como pivote.
#   2. Se recorre el sub-arreglo desde 'bajo' hasta 'alto - 1'.
#   3. Cada elemento menor o igual al pivote se mueve a la
#      izquierda del índice 'i' (usando un swap).
#   4. Al final, el pivote se coloca en su posición definitiva
#      (entre los menores y los mayores).
#   5. Se retorna el índice donde quedó el pivote.
#
# Complejidad:  O(n) por llamada.
# ------------------------------------------------------------
def particion(lista: list, bajo: int, alto: int) -> int:
    """
    Reorganiza el sub-arreglo lista[bajo..alto] en torno al pivote
    y devuelve el índice final del pivote.
    """
    pivote = lista[alto]      # El pivote es el último elemento
    i = bajo - 1              # Índice del elemento más pequeño encontrado

    for j in range(bajo, alto):
        # Si el elemento actual es menor o igual al pivote,
        # se intercambia con la posición i+1 para acumularlo
        # a la izquierda.
        if lista[j] <= pivote:
            i += 1
            # --- SWAP ---
            lista[i], lista[j] = lista[j], lista[i]

    # Colocar el pivote en su posición correcta:
    # todos los elementos a su izquierda son ≤ pivote
    # todos los elementos a su derecha  son >  pivote
    lista[i + 1], lista[alto] = lista[alto], lista[i + 1]

    return i + 1   # Índice definitivo del pivote


# ------------------------------------------------------------
# FUNCIÓN: quicksort
# ------------------------------------------------------------
# Implementación recursiva del algoritmo Quicksort.
#
# ESTRATEGIA "Divide y vencerás":
#   1. DIVIDIR  → se llama a particion() para ubicar el pivote
#                 en su lugar correcto y dividir el arreglo en
#                 dos sub-arreglos: izquierdo (menores) y
#                 derecho (mayores).
#   2. CONQUISTAR → se aplica Quicksort recursivamente a cada
#                   sub-arreglo.
#   3. COMBINAR → no se necesita: al ordenar in-place, cuando
#                 todas las recursiones terminan el arreglo
#                 completo ya está ordenado.
#
# Complejidad temporal:
#   - Mejor caso  : O(n log n)  – pivote siempre en el centro
#   - Caso promedio: O(n log n)
#   - Peor caso   : O(n²)       – lista ya ordenada con este esquema
# Complejidad espacial: O(log n) por la pila de recursión.
# ------------------------------------------------------------
def quicksort(lista: list, bajo: int, alto: int) -> None:
    """
    Ordena in-place el sub-arreglo lista[bajo..alto] usando Quicksort.
    La función modifica la lista directamente (no retorna una nueva).
    """
    # CASO BASE: si 'bajo' >= 'alto', el sub-arreglo tiene 0 ó 1 elemento
    # → ya está ordenado, no hay nada que hacer.
    if bajo < alto:

        # PASO 1 – Particionar: ubica el pivote y obtiene su índice.
        indice_pivote = particion(lista, bajo, alto)

        # PASO 2 – Recursión izquierda: ordena los elementos MENORES al pivote.
        quicksort(lista, bajo, indice_pivote - 1)

        # PASO 3 – Recursión derecha: ordena los elementos MAYORES al pivote.
        quicksort(lista, indice_pivote + 1, alto)


# ------------------------------------------------------------
# FUNCIÓN: mostrar_lista
# ------------------------------------------------------------
# Muestra la lista con formato visual, separando elementos con
# comas y encerrándolos entre corchetes.
# ------------------------------------------------------------
def mostrar_lista(lista: list, etiqueta: str) -> None:
    """Imprime la lista con una etiqueta descriptiva."""
    elementos = ", ".join(str(n) for n in lista)
    print(f"  {etiqueta}: [{elementos}]")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================
def main():
    print("=" * 60)
    print("   LABORATORIO #3 – ALGORITMO QUICKSORT")
    print("   Estructura de Datos II  |  UTP – Colón")
    print("=" * 60)

    # ----------------------------------------------------------
    # PASO 1: Generar 20 números aleatorios en el rango [1, 100]
    # ----------------------------------------------------------
    CANTIDAD = 20
    lista_original = generar_lista(CANTIDAD)

    # Hacemos una copia para no perder la lista original al ordenar,
    # ya que quicksort modifica la lista in-place.
    lista_para_ordenar = lista_original.copy()

    print(f"\n  Números generados: {CANTIDAD}  |  Rango: 1 – 100\n")

    # ----------------------------------------------------------
    # PASO 2: Mostrar la lista original (desordenada)
    # ----------------------------------------------------------
    mostrar_lista(lista_original, "Lista ORIGINAL (desordenada)")

    # ----------------------------------------------------------
    # PASO 3: Aplicar Quicksort y medir el tiempo de ejecución
    # ----------------------------------------------------------
    inicio = time.perf_counter()
    quicksort(lista_para_ordenar, 0, len(lista_para_ordenar) - 1)
    fin = time.perf_counter()

    tiempo_ms = (fin - inicio) * 1_000   # Convertir a milisegundos

    # ----------------------------------------------------------
    # PASO 4: Mostrar la lista ordenada
    # ----------------------------------------------------------
    mostrar_lista(lista_para_ordenar, "Lista ORDENADA  (Quicksort)")

    # ----------------------------------------------------------
    # PASO 5: Estadísticas adicionales
    # ----------------------------------------------------------
    print("\n" + "-" * 60)
    print("  ESTADÍSTICAS")
    print("-" * 60)
    print(f"  Valor mínimo  : {lista_para_ordenar[0]}")
    print(f"  Valor máximo  : {lista_para_ordenar[-1]}")
    print(f"  Tiempo de ejec: {tiempo_ms:.6f} ms")
    print(f"  Complejidad   : O(n log n) caso promedio")
    print("=" * 60)


# Punto de entrada: solo ejecutar si se corre directamente este archivo
if __name__ == "__main__":
    main()
