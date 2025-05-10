# Function to print a separator
def print_separator(title):
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40 + "\n")

# Ejercicio 1
print_separator("Actividad 1 - ¿Es mayor de edad?")
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

# Ejercicio 2
print_separator("Actividad 2 - Calificaciones")
calificacion = float(input("Ingrese su calificación: "))
if calificacion >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3
print_separator("Actividad 3 - Solo pares")
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# Ejercicio 4
print_separator("Actividad 4 - Categorías por edad")
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")
else:
    print("Error ingreso de edad")

# Ejercicio 5
print_separator("Actividad 5 - Longitud de contraseña")
contrasena = input("Ingrese su contraseña: ")
if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6
print_separator("Actividad 6 - Uso de la librería statistics")
#imports para el ejercicio
from statistics import mode, median, mean
import random

#listado numeros aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#calculos estadisticos
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

#calculo de sesgos

#positivo media > mediana y mediana > moda
if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana and mediana == moda:
    print("Sin sesgo")
else:
    print("Indeterminado")      

#Ejercicio 7
print_separator("Actividad 7 - ¿Termina en vocal?")

# Variables auxiliares
listadoVocales = ['a', 'e', 'i', 'o', 'u']

palabra = input("Ingrese una palabra: ")
if palabra[-1].lower() in listadoVocales:
    print(palabra +"!")
else:
    print(palabra)

# Ejercicio 8
print_separator("Actividad 8 - ¿Cómo prefiere su nombre?")
nombre = input("Ingrese su nombre: ")
print("1- Si quiere su nombre en mayúsculas. Por ejemplo JUAN")
print("2- Si quiere su nombre en minúsculas. Por ejemplo juan")
print("3- Si quiere su nombre con primera letra mayúsculas. Por ejemplo Juan")
opcion = int(input("Ingrese una opción: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción incorrecta")

# Ejercicio 9
print_separator("Actividad 9 - Magnitud de terremoto")
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3.0:
    print("Muy leve (imperceptible)")
elif magnitud >= 3.0 and magnitud < 4.0:
    print("Leve (ligeramente perceptible)" )
elif magnitud >= 4.0 and magnitud < 5.0:
    print("Moderado (sentido por las personas, pero generalmente no causa daños)")
elif magnitud >= 5.0 and magnitud < 6.0:
    print("Fuerte (puede causar daños estructuras débiles)")
elif magnitud >= 6.0 and magnitud < 7.0:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7.0:
    print("Extremo (puede causar graves daños a gran escala)")
else:
    print("Error ingreso de magnitud")

# Ejercicio 10
print_separator("Actividad 10 - Estación del año")
hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))
if hemisferio == 'N':
    if (mes == 3 and dia >= 21) or (mes > 3 and mes < 6) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (mes > 6 and mes < 9) or (mes == 9 and dia <= 20):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (mes > 9 and mes < 12) or (mes == 12 and dia <= 20):
        print("Otoño")
    elif (mes == 12 and dia >= 21) or (mes < 3) or (mes == 3 and dia <= 20):
        print("Invierno")
    else:
        print("Error ingreso de fecha")
elif hemisferio == 'S':
    if (mes == 3 and dia >= 21) or (mes > 3 and mes < 6) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (mes > 6 and mes < 9) or (mes == 9 and dia <= 20):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (mes > 9 and mes < 12) or (mes == 12 and dia <= 20):
        print("Primavera")
    elif (mes == 12 and dia >= 21) or (mes < 3) or (mes == 3 and dia <= 20):
        print("Verano")
    else:
        print("Error ingreso de fecha")
else:
    print("Error ingreso de Hemisferio")