# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda
if numero_1 > numero_2:
    print(numero_1, 'es mayor que', numero_2)
else:  
    print(numero_2, 'es mayor que', numero_1)

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso
if numero_1 > 0:
    print (numero_1, 'es positivo')
elif numero_1 < 0:
    print (numero_1, 'es negativo')
else:
    print (numero_1, 'es igual a cero')        
# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición
if numero_1 > 0 and numero_1 < 100:
    print (numero_1, 'es mayor a cero y menor que 100')
elif numero_1 < 0 and numero_1 > -100:
    print (numero_1, 'es menor a cero y mayor que -100')
elif numero_1 < -100:
    print (numero_1, 'es menor a cero y menor que -100')
else:
    print (numero_1, 'es mayor a 100')

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición
if numero_1 < 10 or numero_2 > -2:
    print (numero_1, 'es menor que 10 y', numero_2, 'es mayor que -2' )
elif numero_1 > 10 or numero_2 < -2:
    print (numero_1, 'es mayor que 10 y', numero_2, 'es menor que -2')

# Fin del ejercicio.