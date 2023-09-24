import random

def matriz():
    m = [[random.randint(1, 1000) for _ in range(10)] for _ in range(5)]
    for fila in m:
        print(fila)
    return m

def max(m):
    maximo = m[0][0]
    fila_max = 0
    columna_max = 0
    for i in range(5):
        for j in range(10):
            if m[i][j] > maximo:
                maximo = m[i][j]
                fila_max = i
                columna_max = j
    return maximo, (fila_max, columna_max)

def min(m):
    minimo = m[0][0]
    fila_min = 0
    columna_min = 0
    for i in range(5):
        for j in range(10):
            if m[i][j] < minimo:
                minimo = m[i][j]
                fila_min = i
                columna_min = j
    return minimo, (fila_min, columna_min)

def maxmin(m):
    lista = [numero for fila in m for numero in fila]
    matrizo = sorted(lista, reverse=True)
    matrizf = []
    print("\nLa matriz ordenada de mayor a menor es:")
    for i in range(5):
        fila = []
        for j in range(10):
            fila.append(matrizo.pop(0))
        matrizf.append(fila)
    
    for fila in matrizf:
        print(fila)

def main():
    m = matriz()
    maximo, posicionmax = max(m)
    minimo, posicionmin = min(m)
    print("\nEl número más alto es", maximo, ", su posición es", posicionmax)
    print("El número más bajo es", minimo, ", su posición es", posicionmin)
    maxmin(m)

if __name__ == "__main__":
    main()
