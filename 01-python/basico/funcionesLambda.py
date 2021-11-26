# lambda

lista = [1, 2, 3, 4, 5, 6]

# def par(numero):
#     resultado = (numero % 2) == 0
#     return resultado


# filtro = filter(par, lista)
# pares = list(filtro)
# print(pares)

filtro = filter(lambda numero: (numero % 2) == 0, lista)
pares = list(filtro)
print(pares)
