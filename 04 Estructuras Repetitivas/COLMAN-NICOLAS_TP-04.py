# Function to print a separator
def print_separator(title):
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40 + "\n")

# Ejercicio 1
print_separator("Actividad 1 - Números del 0 al 100")
for i in range(0, 101):
    print(str(i))

# Ejercicio 2
print_separator("Actividad 2 - Cantidad de dígitos")
numero = int(input("Ingrese un número entero: "))
cantidad_digitos = len(str(abs(numero)))
print(f"La cantidad de dígitos del número {numero} es: {cantidad_digitos}")

# Ejercicio 3
print_separator("Actividad 3 - Sumar números enteros")
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))   
suma = 0

if valor1 < valor2:
    for i in range(valor1 + 1, valor2):
        suma += i
else:
    for i in range(valor2 + 1, valor1):
        suma += i
print(f"La suma de los números comprendidos entre {valor1} y {valor2} es: {suma}")

# Ejercicio 4
print_separator("Actividad 4 - Sumar valores hasta ingresar 0")
suma = 0  
valor = int(input("Ingrese un valor (0 para salir): "))
while valor != 0:
    suma += valor
    valor = int(input("Ingrese un valor (0 para salir): "))
print(f"La suma de los valores ingresados es: {suma}") 

# Ejercicio 5
print_separator("Actividad 5 - Adivinar número aleatorio")
import random
numero_aleatorio = random.randint(0, 9)
intentos = 0
numero_usuario = int(input("Adivina el número entre 0 y 9: "))
while numero_usuario != numero_aleatorio:
    intentos += 1
    if numero_usuario < numero_aleatorio:
        print(Fore.RED + "El número es mayor.")
    else:
        print(Fore.BLUE + "El número es menor.")
    numero_usuario = int(input("Intenta nuevamente: "))
intentos += 1
print(f"¡Felicidades! Adivinaste el número correcto en {intentos} intentos.")

# Ejercicio 6
print_separator("Actividad 6 - Números pares entre 0 y 100 de forma decreciente")
for i in range(100, -1, -2):
    print(str(i))

# Ejercicio 7

print_separator("Actividad 7 - Sumar números hasta un número dado")
numero = int(input("Ingrese un número entero positivo: "))
suma = 0
while numero < 0:
    print(Fore.RED + "El número debe ser positivo.")
    numero = int(input("Ingrese un número entero positivo: "))   
for i in range(0, numero + 1):
    suma += i
print(f"La suma de los números entre 0 y {numero} es: {suma}")

# Ejercicio 8
print_separator("Actividad 8 - Contar números")
cantidad_numeros = 100
cantidad_pares = 0
cantidad_impares = 0
cantidad_positivos = 0
cantidad_negativos = 0
for i in range(cantidad_numeros):
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1
    if numero > 0:
        cantidad_positivos += 1
    elif numero < 0:
        cantidad_negativos += 1
print(f"Cantidad de números pares: {cantidad_pares}")
print(f"Cantidad de números impares: {cantidad_impares}")
print(f"Cantidad de números positivos: {cantidad_positivos}")
print(f"Cantidad de números negativos: {cantidad_negativos}")

# Ejercicio 9
print_separator("Actividad 9 - Calcular la media")
cantidad_numeros = 100
suma = 0
for i in range (cantidad_numeros):
    numero = int(input("Ingrese un número entero: "))
    suma += numero
print(f"La media de los números ingresados es: {suma / cantidad_numeros}")

# Ejercicio 10
print_separator("Actividad 10 - Invertir número")
numero = int(input("Ingrese un número entero: "))
numero_invertido = 0

signo = -1 if numero < 0 else 1
numero = abs(numero)
while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero //= 10
numero_invertido *= signo

print(f"El número invertido es: {numero_invertido}")