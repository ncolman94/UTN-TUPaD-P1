# Function to print a separator
def print_separator(title):
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40 + "\n")

# Ejercicio 1
print_separator("Actividad 1 - Lista de múltiplos de 4 entre 1 y 100")
numeros = list(range(1, 101))
multiplos_de_4 = [num for num in numeros if num % 4 == 0]

print("Lista de números del 1 al 100: ")
print(f"{numeros}")
print("Números múltiplos de 4: ")
print(f"{multiplos_de_4}")


# Ejercicio 2
print_separator("Actividad 2 - Antepenúltimo elemento de una lista aleatoria")
import random
elementos_aleatorios = [random.choice(['Hola', 42, 3.14, True, 'Mundo']) for _ in range(10)]
print("Lista de elementos aleatorios: ")
print(f"{elementos_aleatorios}")
print()
antepenultimo_elemento = elementos_aleatorios[-3]
print(f"Antepenúltimo elemento: ")
print(f"{antepenultimo_elemento}")

# Ejercicoo 3
print_separator("Actividad 3 - Lista vacía y agregar valores aleatorios")
lista = []
valores_aleatorios = ['UTN', 'Progra I', 'Python']
for valor in valores_aleatorios:
    lista.append(valor)
print("Lista generada: ")
print(f"{lista}")

# Ejercicio 4
print_separator("Actividad 4 - Reemplazo de elementos en una lista")
lista_animales = ["perro", "gato", "conejo", "pez"]
print("Lista inicial: ")
print(f"{lista_animales}")
lista_animales[1] = "loro"
lista_animales[-1] = "oso"
print()
print("Nueva lista con cambiios: ")
print(f"{lista_animales}")

# Ejercicio 5
print_separator("Actividad 5 - ¿Qué hace este código?")
bloque_codigo = "numeros = [8, 15, 3, 22, 7]\n" \
                "numeros.remove(max(numeros)\n" \
                "print(numeros)"
print("Bloque de código: ")
print(bloque_codigo)
print()
print("Descripción: ")
print("1. Crea una lista llamada 'numeros' con los valores 8, 15, 3, 22, 7\n"
    "2. Determina el elemento mayor de la lista y lo remueve.\n"
    "4. Imprime la lista resultante.")

# Ejercicio 6
print_separator("Actividad 6 - Lista con saltos de 5 en 5")
numeros_con_saltos = list(range(10, 31, 5))
print("Lista de números del 10 al 30 con saltos de 5 en 5: ")
print(f"{numeros_con_saltos}")
print()
print("Resultados:")
print(f"Primer elemento: {numeros_con_saltos[0]}, segundo elemento: {numeros_con_saltos[1]}")

# Ejercicio 7
print_separator("Actividad 7 - Modificación de elementos en una lista")
lista_autos = ["sedan", "polo", "suran", "gol"]
print("Lista inicial: ")
print(f"{lista_autos}")
lista_autos[1] = "fiesta"
lista_autos[2] = "focus"
print()
print("Lista modificada: ")
print(f"{lista_autos}")

# Ejercicio 8
print_separator("Actividad 8 - Lista de dobles")
dobles = []
for num in [5, 10, 15]:
    dobles.append(num * 2)
print("Lista de dobles: ")
print(f"{dobles}")

# Ejercicio 9
print_separator("Actividad 9 - Compras de diferentes clientes")
compras = [
    ["pan", "leche"],
    ["arroz", "fideos", "salsa"],
    ["agua"]
]
print("Lista de compras original: ")
for i, cliente in enumerate(compras):
    print(f"Cliente {i + 1}: {cliente}")

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print()
print("Lista de compras modificada: ")
for i, cliente in enumerate(compras):
    print(f"Cliente {i + 1}: {cliente}")

# Ejercicio 10
print_separator("Actividad 10 - Lista anidada")
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print("Lista anidada: ")
print(f"{lista_anidada}")