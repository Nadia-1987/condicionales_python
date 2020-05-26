#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica con números
    


    numero_1 = int(input('ingrese el primer numero:\n'))
    numero_2 = int(input('ingrese el segundo numero:\n'))

    resta = numero_1 - numero_2
    if resta > 0:
        print('el numero es positivo')
    elif resta < 0:
        print('el numero es negativo')
    else:
        print('el numero es cero')

        
    

def ej2():
# Ejercicios de práctica con números

    numero_1 = int(input('Ingrese un numero entero:\n'))
    numero_2 = int(input('Ingrese un numero entero:\n'))
    numero_3 = int(input('Ingrese un numero entero:\n'))

    if numero_1 % 2 == 0:
        print('el numero es par')
    else:
        print('el numero es impar')
  
    if numero_2 % 2 == 0:
        print('el numero es par')
    else:
         print('el numero es impar')

    if numero_3 % 2 == 0:
        print('el numero es par')
    else:
        print('el numero es impar')

def ej3():
    # Ejercicios de práctica con números

    primer_numero = 10
    segundo_numero = 20
    suma = primer_numero + segundo_numero
    resta = primer_numero - segundo_numero
    multiplicacion = primer_numero * segundo_numero
    division = primer_numero / segundo_numero
    exponente = primer_numero ** segundo_numero
    
    operador = str(input('Ingrese el simbolo de la operacion que desee operar:\n'))
    if operador == '+':
        print('el resultado de la suma entre',numero_1,'y',numero_2,'es',suma)
    elif operador == '-':
        print('el resultado de la resta entre',numero_1,'y',numero_2,'es',resta)
    elif operador == '*':
        print('el resultado de la multiplicacion entre',numero_1,'y',numero_2,'es',multiplicacion)
    elif operador == '/':
        print('el resultado de la division entre',numero_1,'y',numero_2,'es',division)
    elif operador == '**':
        print('el resultado del exponente de',numero_1,'a',numero_2,'es',exponente) 



    #Se debe efectuar el cálculo correcto según la operación ingresada por consola
    #Imprimir en pantalla la operación realizada y el resultado
    

    

def ej4():
    # Ejercicios de práctica con cadenas
    
    

    palabra_1 = str(input('Ingrese palabra 1'))
    palabra_2 = str(input('Ingrese palabra 2'))
    palabra_3 = str(input('Ingrese palabra 3'))
    consulta_orden = int(input('Ingrese 1 para ordenar alfabeticamente o 2 por longitud de palabra: '))

    
    #Luego el programa debe consultar al usuario como quiere ordenar las palabras
    #1 - Ordenar por orden alfabético (usando el operador ">")
    #2 - Ordenar por cantidad de letras (longitud de la palabra)

    #Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    #e imprimir en pantalla de la mayor a la menor

    #Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    #e imprimir en pantalla de la mayor a la menor

  

def ej5():
    # Ejercicios de práctica con números
       
    

    temperatura_1 = int(input('Ingrese temperatura 1'))
    temperatura_2 = int(input('Ingrese temperatura 2'))
    temperatura_3 = int(input('Ingrese temperatura 3'))

    if temperatura_1 > temperatura_2 and temperatura_1 > temperatura_3:
        print(temperatura_1,'es la mayor') 
    else:
        if temperatura_2 > temperatura_1 and temperatura_2 > temperatura_3:
            print(temperatura_2,'es la mayor')
        else:
            if temperatura_3 > temperatura_1 and temperatura_3 > temperatura_2:
                print(temperatura_3,'es la mayor')

    

if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
