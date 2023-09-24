def lista():
    f=open("Alimentos.txt","rt")
    line= f.readlines()
    f.close()
    return line

def lista():
    f = open("Alimentos.txt", "rt")
    lineas = f.readlines()
    f.close()
    return lineas
def alimento(lineas):
    for i, linea in enumerate(lineas):
        alimentos = linea.split(",")
        if len(alimentos) > 1:
            print(f"{i + 1}. {alimentos[1]}")
    
    opcion = input("Escoja un alimento de la lista (número): ")
    return opcion

def calcular_iva(valor_neto, tasa_iva):
    return valor_neto / (1 + (tasa_iva))

def main():
    lineas = lista()
    opcion = alimento(lineas)
    opcion = int(opcion) - 1  
    if 0 <= opcion < len(lineas):
        alimentos = lineas[opcion].split(",")
        if len(alimentos) == 3 and float(alimentos[2]) > 0:  
            valor_neto = float(input("Ingrese el valor neto del producto: "))
            tasa_iva = float(alimentos[2])
            valor_base = calcular_iva(valor_neto, tasa_iva)
            print(f"El valor base es: ${round(valor_base,2)}")
        else:
            print("El alimento seleccionado no tiene IVA.")
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    main()
