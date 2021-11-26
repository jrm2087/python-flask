# conjuntos

conjunto = set()
print(conjunto)

# añadir
conjunto.add(1)
conjunto.add(2)
conjunto.add(3)
conjunto.add('Hola')
print(conjunto)

# eliminar
conjunto.discard('Hola')
print(conjunto)

# solo permite valores unicos
conjunto.add(9)
conjunto.add(9)
conjunto.add(9)
print(conjunto)

lista = [1, 2, 3, 4, 4, 4, 1, 1, 3, 5, 5, 5]
conjunto = set(lista)
print(conjunto)
