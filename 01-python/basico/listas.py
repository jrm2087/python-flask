lista = [1, 2, 3]
print(lista)

lista = ['Jose', 2, True]
print(lista)

elemento = lista[0]
print(elemento)

elemento = lista[-1]
print(elemento)

elemento = lista[2:4]
print(elemento)

lista2 = ['amarillo', 'azul', 'rojo']

lista.append(lista2)
print(lista)

elemento = lista[3]
print(elemento)

# ------------- extend -----
lista = ['Jose', 2, True]
lista2 = ['amarillo', 'azul', 'rojo']
lista.extend(lista2)
print(lista)

# -----
lista = [1, 2, 'negro', 3, 'Jose']
print(lista)

# eliminar ultimo elemento de la lista
lista.pop()
print(lista)

# eliminar primer elemento
lista.pop(0)
print(lista)

# dar vuelta a una lista
lista = [1, 2, 'negro', 3, 'Jose']
print(lista)

lista.reverse()
print(lista)

# ordernar lista
lista = [3, 5, 6, 7, 1, 3, 2, 0, 9, 10, 4]
print(lista)

lista.sort()
print(lista)

# listas anidadas
lista = [1, 2, 3, 4, ['negro', 'blanco']]
print(lista)

elemento = lista[4][0]
print(elemento)

# lista de comprension
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_nueva = [elemento[0] for elemento in matriz]
print(lista_nueva)
