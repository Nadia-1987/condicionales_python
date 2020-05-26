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

  if (numero_1 + numero_1) / 2 == > 0:
    print('el numero es positivo')
  elif (numero_1 + numero_2) / 2 == < 0:
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
    print('el numero es impar')´
  
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
    
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    

    '''

def ej4():
    # Ejercicios de práctica con cadenas
    
    

    palabra_1 = str(input('Ingrese palabra 1'))
    palabra_2 = str(input('Ingrese palabra 2'))
    palabra_3 = str(input('Ingrese palabra 3'))

    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor

  '''

def ej5():
    # Ejercicios de práctica con números
       
    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    temperatura_1 = int(input('Ingrese temperatura 1'))
    temperatura_2 = int(input('Ingrese temperatura 2'))
    temperatura_3 = int(input('Ingrese temperatura 3'))

    En cada caso imprimir en pantalla el resultado  

    '''

if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
