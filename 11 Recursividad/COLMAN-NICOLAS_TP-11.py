# Function to print a separator
def print_separator(title):
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40 + "\n")

def validar_entero_positivo(valor):
    while True:
        try:
            numero = int(valor)
            if numero < 0:
                raise ValueError("El número debe ser positivo.")
            return numero
        except (ValueError, TypeError):
            print("Debe ingresar un número entero positivo.")
            valor = input("Ingrese un número entero positivo: ").strip()

## TP Entrega Recursividad ##

# Ejercicio 1
print_separator("Actividad 1 - Factorial Recursivo")

def factorial_recursivo(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial_recursivo(numero - 1)

# Solicitar al usuario un número entero positivo
calculo_factorial = input("Ingrese un número entero positivo para calcular su factorial: ")
entero_valido = validar_entero_positivo(calculo_factorial)

for i in range(1, entero_valido + 1):
    print(f"El factorial de {i} es {factorial_recursivo(i)}")

# Ejercicio 2
print_separator("Actividad 2 - Serie de Fibonacci Recursiva")
def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Solicitar al usuario un número entero positivo
calculo_fibonacci = input("Ingrese un número entero positivo para calcular la serie de Fibonacci: ")
entero_valido_fibonacci = validar_entero_positivo(calculo_fibonacci)
print(f"Serie de Fibonacci hasta la posición {entero_valido_fibonacci}:")
for i in range(entero_valido_fibonacci + 1):
    print(f"Fibonacci({i}) = {fibonacci_recursivo(i)}")

# Ejercicio 3
print_separator("Actividad 3 - Potencia Recursiva")
def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

# Solicitar al usuario la base y el exponente
base = input("Ingrese la base (número entero positivo): ")
exponente = input("Ingrese el exponente (número entero positivo): ")
base_valida = validar_entero_positivo(base)
exponente_valido = validar_entero_positivo(exponente)

resultado = potencia_recursiva(base_valida, exponente_valido)
print(f"{base_valida} elevado a {exponente_valido} es {resultado}")

# Ejercicio 4
print_separator("Actividad 4 - Decimal a Binario Recursivo")
def decimal_a_binario_recursivo(numero):
    if numero == 0:
        return ""
    else:
        return decimal_a_binario_recursivo(numero // 2) + str(numero % 2)
# Solicitar al usuario un número entero positivo
calculo_binario = input("Ingrese un número entero positivo para convertir a binario: ")
entero_valido_binario = validar_entero_positivo(calculo_binario)
resultado_binario = decimal_a_binario_recursivo(entero_valido_binario)

# Si el resultado es una cadena vacía, significa que el número es 0
if resultado_binario == "":
    resultado_binario = "0"

print(f"El número {entero_valido_binario} en binario es: {resultado_binario}")

# Ejercicio 5
print_separator("Actividad 5 - Palíndromo Recursivo")
def es_palindromo_recursivo(palabra):
    # Convertir la palabra a minúsculas y eliminar espacios
    palabra = palabra.lower().replace(" ", "")
    # Caso base: si la longitud de la palabra es 0 o 1, es un palíndromo
    if len(palabra) <= 1:
        return True
    # Comparar el primer y último carácter
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva eliminando el primer y último carácter
    return es_palindromo_recursivo(palabra[1:-1])

# Solicitar al usuario una palabra
calculo_palindromo = input("Ingrese una palabra o frase para verificar si es un palíndromo: ")

# Verificar si es un palíndromo
if es_palindromo_recursivo(calculo_palindromo):
    print(f"La palabra '{calculo_palindromo}' es un palíndromo.")
else:
    print(f"La palabra '{calculo_palindromo}' no es un palíndromo.")

# Ejercicio 6
print_separator("Actividad 6 - Suma de Dígitos Recursiva")
def suma_digitos_recursiva(numero):
    # Caso base: si el número es 0, la suma de sus dígitos es 0
    if numero < 10:
        return numero
    else:
        # Sumar el último dígito y llamar recursivamente con el número sin el último dígito
        return (numero % 10) + suma_digitos_recursiva(numero // 10)
# Solicitar al usuario un número entero positivo
calculo_suma_digitos = input("Ingrese un número entero positivo para calcular la suma de sus dígitos: ")
entero_valido_suma_digitos = validar_entero_positivo(calculo_suma_digitos)
resultado_suma_digitos = suma_digitos_recursiva(entero_valido_suma_digitos)
print(f"La suma de los dígitos de {entero_valido_suma_digitos} es: {resultado_suma_digitos}")

# Ejercicio 7
print_separator("Actividad 7 - Contar Bloques Recursivo")
def contar_bloques_recursivo(n):
    # Caso base: si no hay bloques, no hay pirámide
    if n <= 0:
        return 0
    else:
        # Sumar el número de bloques en el nivel actual y llamar recursivamente para el siguiente nivel
        return n + contar_bloques_recursivo(n - 1)
# Solicitar al usuario el número de bloques en el nivel más bajo
calculo_bloques = input("Ingrese el número de bloques en el nivel más bajo de la pirámide: ")
entero_valido_bloques = validar_entero_positivo(calculo_bloques)
resultado_bloques = contar_bloques_recursivo(entero_valido_bloques)
print(f"El total de bloques necesarios para construir la pirámide con {entero_valido_bloques} bloques en el nivel más bajo es: {resultado_bloques}")

# Ejercico 8
print_separator("Actividad 8 - Contar Dígito Recursivo")
def contar_digito_recursivo(numero, digito):
    # Caso base: si el número es 0, no hay más dígitos que contar
    if numero == 0:
        return 0
    else:
        # Verificar si el último dígito es igual al dígito buscado
        if numero % 10 == digito:
            return 1 + contar_digito_recursivo(numero // 10, digito)
        else:
            return contar_digito_recursivo(numero // 10, digito)
# Solicitar al usuario un número entero positivo y un dígito
calculo_contar_digito = input("Ingrese un número entero positivo: ")
entero_valido_contar_digito = validar_entero_positivo(calculo_contar_digito)
digito = input("Ingrese un dígito (0-9) para contar cuántas veces aparece en el número: ")
digito_valido = validar_entero_positivo(digito)
resultado_contar_digito = contar_digito_recursivo(entero_valido_contar_digito, digito_valido)
print(f"El dígito {digito_valido} aparece {resultado_contar_digito} veces en el número {entero_valido_contar_digito}.")
