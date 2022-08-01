# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
pal_1 = str(input('ingrese la primer palabra:\n'))
pal_2 = str(input('ingrese la segunda palabra:\n'))
pal_3 = str(input('ingrese la tercera palabra:\n'))
# Consulta de operacion
orden = str(input('Ingrese 1 para ordenar alfabeticamente, 2 para ordenar por cantidad de letras:\n'))
# Resolucion alfabetica
if orden == '1':
    if pal_1 < pal_2 and pal_2 < pal_3 :
        print (pal_1, pal_2, pal_3)
    elif pal_2 < pal_1 and pal_1 < pal_3 :
        print (pal_2, pal_1, pal_3)
    elif pal_3 < pal_2 and pal_2 < pal_1 :
        print (pal_3, pal_2, pal_1)
    elif pal_1 < pal_3 and pal_3 < pal_2:
        print (pal_1, pal_3, pal_2)
    elif pal_3 < pal_1 and pal_1 < pal_2:
        print (pal_3, pal_1, pal_2)
    elif pal_2 < pal_3 and pal_3 < pal_1:
        print (pal_2, pal_3, pal_1)
# Resolucion por caracteres
if orden == '2':
    if len (pal_1) > len (pal_2) and len (pal_2) > len (pal_3) :
        print (pal_1, pal_2, pal_3)
    elif len (pal_2) > len (pal_1) and len (pal_1) > len (pal_3) :
        print (pal_2, pal_1, pal_3)
    elif len (pal_3) > len (pal_2) and len (pal_2) > len (pal_1) :
        print (pal_3, pal_2, pal_1)
    elif len (pal_1) > len (pal_3) and len (pal_3) > len (pal_2):
        print (pal_1, pal_3, pal_2)
    elif len (pal_3) > len (pal_1) and len (pal_1) > len (pal_2):
        print (pal_3, pal_1, pal_2)
    elif len (pal_2) > len (pal_3) and len (pal_3) > len (pal_1):
        print (pal_2, pal_3, pal_1)
# Fin del ejercicio
    