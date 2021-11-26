# funciones

# def saludo():
#     print('Hola, buenos días.')
#
#
# saludo()

def sumar(numero1, numero2):
    """
    Esta función suma dos numeros enteros
    Ej. de llamada:
        sumar(5,2)
    """
    if type(numero1) == type(numero2) == type(10):
        resultado = numero1 + numero2
    else:
        resultado = 'Error, debe ser numeros.'
    return resultado


suma = sumar(5, 2)
print(suma)
