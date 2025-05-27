# Function to print a separator
def print_separator(title):
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40 + "\n")

def imprimir_saludo():
    # Función que imprime "Hola Mundo"
    print("Hola Mundo!")

def saludar_usuario(nombre):
    # Función que saluda al usuario por su nombre
    print(f"Hola {nombre}!")

def informacion_personal(nombre, apellido, edad, residencia):
    # Función que imprime la información personal del usuario
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def calcular_area_circulo(radio):
    # Función que calcula el área de un círculo dado su radio
    import math
    area = math.pi * radio ** 2
    return area
def calcular_perimetro_circulo(radio):
    # Función que calcula el perímetro de un círculo dado su radio
    import math
    perimetro = (2 * math.pi * radio)
    return perimetro

def segundos_a_horas(segundos):
    # Función que convierte segundos a horas
    horas = segundos / 3600
    return horas

def tabla_multiplicar(numero):
    print()
    # Función que imprime la tabla de multiplicar de un número
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def operaciones_basicas(primer_numero, segundo_numero):
    # Función que realiza operaciones básicas entre dos números
    suma = primer_numero + segundo_numero
    resta = primer_numero - segundo_numero
    multiplicacion = primer_numero * segundo_numero
    division = primer_numero / segundo_numero if segundo_numero != 0 else "Error: División por cero"

    return suma, resta, multiplicacion, division

def calcular_imc(peso, altura):
    # Función que calcula el IMC (Índice de Masa Corporal)
    imc = peso / (altura ** 2)
    return imc

def imprimir_imc(imc):
    # Clasificación del IMC
    # Según la Organización Mundial de la Salud (OMS): 
    # Referencia https://www.tuasaude.com/es/imc/

    #Bajo peso	Menos de 18,4 
    #Peso normal	Entre 18,5 y 24,9
    #Sobrepeso	Entre 25 y 29,9
    #Obesidad	30 o más

    if imc < 18.5:
        print("Clasificación - Bajo peso")
    elif 18.5 <= imc < 24.9: 
        print("Clasificación - Peso normal")
    elif 25 <= imc < 29.9:
        print("Clasificación - Sobrepeso")
    else:
        print("Clasificación - Obesidad")     

def celsius_a_fahrenheit(celsius):
    # Función que convierte Celsius a Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def calcular_promedio(valor_1, valor_2, valor_3):
    # Función que calcula el promedio de tres valores
    promedio = (valor_1 + valor_2 + valor_3) / 3
    return promedio

# Ejercicio 1 implementación función Hola Mundo
print_separator("Actividad 1 - Hola Mundo")

#Llamada a función auxiliar
imprimir_saludo()

# Ejercicio 2 saludar usuario no nombre por parámetro
print_separator("Actividad 2 - Saludo al usuario")
nombre = input("Ingrese su nombre: ")

#Llamada a función auxiliar
saludar_usuario(nombre)

# Ejercicio 3 información personal con formato
print_separator("Actividad 3 - Información personal")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")

#Llamada a función auxiliar
informacion_personal (nombre, apellido, edad, residencia)

#Ejercicio 4 cálculo de área y perímetro de un circulo
print_separator("Actividad 4 - Cálculo de área y perímetro de un círculo")

radio = float(input("Ingrese el radio del círculo: "))

#Llamada a función auxiliar
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

# Se establecen dos decimales para el área y perímetro
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

# Ejercicio 5 conversión de segundos a horas
print_separator("Actividad 5 - Conversión de segundos a horas")
segundos = int(input("Ingrese la cantidad de segundos: "))

#Llamada a función auxiliar
horas = segundos_a_horas(segundos)

# Se establece dos decimales para la conversión
print(f"{segundos} segundos son {horas:.2f} horas.")

# Ejercicio 6 tabla de multiplicar por pantalla para dato recibido por parámetro
print_separator("Actividad 6 - Tabla de multiplicar")
numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: ")) 

# Llamada a función auxiliar
tabla_multiplicar(numero)

# Ejercicio 7 operaciones basicas 
print_separator("Actividad 7 - Operaciones básicas")
primer_numero = float(input("Ingrese el primer número: "))
segundo_numero = float(input("Ingrese el segundo número: "))

# Llamadas a funciones auxiliares
calculos = operaciones_basicas (primer_numero, segundo_numero)

# Presentación de resultados
print(f"La suma es: {calculos[0]}")
print(f"La resta es: {calculos[1]}")  
print(f"La multiplicación es: {calculos[2]}")
if segundo_numero != 0:
    print(f"La división es: {calculos[3]}")
else:
    print("Error, no es posible división por cero")

# Ejercicio 8 calculo e IMC
print_separator("Actividad 8 - Cálculo de IMC")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

# Llamada a función auxiliar
imc = calcular_imc(peso, altura)

# Presentación de resultados
print(f"Su IMC es: {imc:.2f}")

# Llamada a función auxiliar para imprimir el IMC
imprimir_imc (imc)

# Ejericio 9 conversión de celsius a fahrenheit
print_separator("Actividad 9 - Conversión Celsius a Fahrenheit")
celsius = float(input("Ingrese la temperatura en Celsius: "))

# Llamada a función auxiliar
fahrenheit = celsius_a_fahrenheit (celsius) 

# Presentación de resultados
# Se establece dos decimales para la conversión
print(f"{celsius}°C son {fahrenheit:.2f}°F")

# Ejercicio 10 cálculo de promedio
print_separator("Actividad 10 - Cálculo de promedio")
valor_1 = float(input("Ingrese el primer valor: "))
valor_2 = float(input("Ingrese el segundo valor: "))
valor_3 = float(input("Ingrese el tercer valor: "))

promedio = calcular_promedio(valor_1, valor_2, valor_3)

#Presentación de resultados
print(f"El promedio de los tres valores es: {promedio:.2f}")