# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv
from types import DynamicClassAttribute


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    csvfile = open(archivo, 'r')
    stock = list(csv.DictReader(csvfile))
    tornillos_totales = 0

    for i in range(len(stock)):
            lista = stock[i]
            for k, v in lista.items():
                if k == 'tornillos':
                    cant_tornillos = v
                    cantidad = int(cant_tornillos)
                    tornillos_totales += cantidad 
        
    print('Tornillos Totales: ', tornillos_totales)

    csvfile.close()


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    csvfile = open('propiedades.csv', 'r')
    departamentos = list(csv.DictReader(csvfile))

    dos_ambientes = 0
    tres_ambientes = 0
    sin_definir = 0

    for i in range(len(departamentos)):
        for k, v in departamentos[i].items():
            if k == 'ambientes':
                if v == '2':
                    dos_ambientes += 1
                
                elif v == '3':
                    tres_ambientes += 1

                else:
                    sin_definir += 1
            
    
    print("Cantidad de departamentos de 2 ambientes: ", dos_ambientes)
    print("Cantidad de departamentos de 3 ambientes: ", tres_ambientes)
    print("Cantidad de departamentos restantes: ", sin_definir)


    csvfile.close()
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
