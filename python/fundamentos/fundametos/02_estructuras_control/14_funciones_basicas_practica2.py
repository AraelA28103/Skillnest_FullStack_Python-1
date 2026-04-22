import os
# Funciones basicas practica 2


# ejercicio 1
# Calcula experiencia
def multiplica_por_2(num):
    result = []
    for i in range(num + 1):
        result.append(1 * 2)
    return result
def ejercicio1():
    result1 = multiplica_por_2(5)
    print(result1)
# Debe retornar: [0, 2, 4, 6, 8, 10]


# ejercicio 2
# Analiza publicaciones
def suma_y_resta(lista):
    suma = lista[0] + lista[1]
    resta = lista[0] - lista[1]
    print(suma)
    return resta
def ejercicio():
    resultado2 = suma_y_resta([120, 115]) 
# Imprime: 235, Retorna: 5

# ejercicio 3
# Puntaje ajustado
def sumatoria_menos_longitud(lista):
    total = sum(lista)
    longitud = len(lista)
    return total - longitud
def ejercicio():
    resultado3 = sumatoria_menos_longitud([10, 5, 3, 7])
# Suma total = 25, longitud = 4, debe retornar: 21


# ejercicio 4
# Ajusta visualizaciones
def valores_multiplicados_segundo():
    pass
valores_multiplicados_segundo([100, 3, 50, 20])
# Imprime: 4 y retorna: [300, 9, 150, 60]

def valores_multiplicados_segundo():
    pass
valores_multiplicados_segundo([100])
# Imprime: 1 y retorna: []


# ejercicio 5
# Genera precio fijo
def valor_multiplicado_longitud():
    pass
valor_multiplicado_longitud(5,2)
# Debe retornar: [10, 10]

def valor_multiplicado_longitud():
    pass
valor_multiplicado_longitud(7, 5)
# Debe retornar: [35, 35, 35, 35, 35]


def limpiar_consola():
    os.system('cls')

continuar = True
while continuar: 
    print("\n---Ejercicios Python---")
    print("---Ejercicio 1---")
    print("---Ejercicio 2---")
    print("---Ejercicio 3---")
    print("---Ejercicio 4---")
    print("---Ejercicio 5---")
    opcion = input("\n---Elije una opción: (1-5) (0 para salir)")
    if opcion == "1":
        limpiar_consola()
        print("\nEjecutar ejercicio 1: ")
        multiplica_por_2()
    elif opcion == "2":
        limpiar_consola()
        print("\nEjecutar ejercicio 2: ")
        suma_y_resta()
    elif opcion == "3":
        limpiar_consola()
        print("\nEjecutar ejercicio 3: ")
        sumatoria_menos_longitud()
    elif opcion == "4":
        limpiar_consola()
        print("\nEjecutar ejercicio 4: ")
        valores_multiplicados_segundo()
    elif opcion == "5":
        limpiar_consola()
        print("\nEjecutar ejercicio 5: ")
        valor_multiplicado_longitud()
    elif opcion == "0":
        limpiar_consola()
        print("Saliendo...")
        continuar = False
    else:
        print("Opción no válido. Intenta otra vez.")