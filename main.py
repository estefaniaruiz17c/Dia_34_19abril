# Listas por comprensión: permite crear listas avanzadas en una misma línea de código.
print("\nListas por comprensión\n")

print()
# Ejercicio 1
print("\n- Ejercicio 1: Multiplicar por 11\n")

# Multiplicar cada elemento de la lista por 11 y almacenarlos en otra lista

# Lista a evaluar
numeros1 = [4,6,2,7,3]
print("\nLista original de números:",numeros1)

# Uso de la lista por comprensión. Para hacerlas, primero escribimos la operación que queremos realizar, a continución designamos el ciclo for para recorrer la lista; todo esto lo encerramos entre corchetes. Al imprimir la nueva lista, veremos la modificación planteada previamente. 
lista_numeros1 = [num*11 for num in numeros1]

# Mostrar la respuesta
print("\nElementos de la lista original multiplicados por 11:",lista_numeros1)


print()
print()
# Ejercicio 2
print("\n- Ejercicio 2: Convertir en mayúscula primera letra de cada palabra\n")

# Convertir en mayúscula primera letra de cada palabra de la lista

# Lista a evaluar
palabras1 = ["sospechoso","policia","investigacion","juicio", "arresto","interrogatorio"]
print("\nLista original:",palabras1)

# Creación de la lista por comprensión
lista_palabras1 = [word.capitalize() for word in palabras1]

# Mostrar la respuesta
print("\nPoner en mayúscula primera letra de cada palabra de la lista original:",lista_palabras1)


print()
print()
# Ejercicio 3
print("\n- Ejercicio 3: Sumar a la lista original un número, se evalúa cada elemento de la lista, y se muestran los menores a 5\n")

# Sumar a la lista original un número, se evalúa cada elemento de la lista, y se muestran los menores a 5

# Lista a evaluar
numeros2 = [-5,0,-2,4,8]
print("\nLista original:",numeros2)

# Creación de la lista por comprensión
lista_numeros2 = [num + 3 for num in numeros2 if num < 3]

# Mostrar la respuesta
print("\nLuego de la lista por comprensión la lista resultante es:",lista_numeros2)


print()
print()
# Ejercicio 4
print("\n- Ejercicio 4: Convertir palabras de una lista en minúscula\n")

# Convertir palabras de una lista en minúscula

# Lista a evaluar
palabras2 = ["BIENVENIDOS","CAMPEONATO","NACIONAL"]
print("\nLista original:",palabras2)

# Creación de la lista por comprensión
lista_palabras2 = [word.lower() for word in palabras2]

# Mostrar la respuesta
print("\nPalabras de la lista original en minúscula:",lista_palabras2)


print()
print()
# Ejercicio 5
print("\n- Ejercicio 5: Sacar la segunda letra de cada palabra de la lista\n")

# Sacar la segunda letra de cada palabra de la lista

# Lista a evaluar
palabras3 = ["SERENO","unido","oculto","pala","ansia","atormentado","mosca"]
print("\nLista original:",palabras3)

# Creación de la lista por comprensión
lista_palabras3 = [word[1] for word in palabras3]

# Mostrar la respuesta
print("\nSegunda letra de cada palabra de la lista original:",lista_palabras3)


print()
print()
# Ejercicio 6
print("\n- Ejercicio 6: Elevar cada número de la lista a la potencia 4 y redondear a 4 decimales\n")

# Elevar cada número de la lista a la potencia 4 y redondear a 4 decimales

# Lista a evaluar
decimales1 = [2.7,0.15,6.7,5.3]
print("\nLista original:",decimales1)

# Creación de la lista por comprensión
lista_decimales1 = [round(deci**4,4) for deci in decimales1 ]

# Mostrar la respuesta
print("\nLuego de la lista por comprensión la lista resultante es:",lista_decimales1)


print()
print()
# Ejercicio 7
print("\n- Ejercicio 7: Encontrar coincidencias entre 2 listas\n")

# Encontrar coincidencias entre 2 listas

# Lista a evaluar
palabras4_universe = ["galaxia","estrella","meteorito","tierra","cometa"]
palabras5_favorito = ["cometa","estrella","helado","casa"]
print("\nLista original 1:",palabras4_universe)
print("\nLista original 2:",palabras5_favorito)

# Creación de la lista por comprensión
lista_palabras4y5 = [word1 for word1 in palabras4_universe for word2 in palabras5_favorito if word1==word2]

# Mostrar la respuesta
print("\nCoincidencias entre las dos listas anteriores:",lista_palabras4y5)

