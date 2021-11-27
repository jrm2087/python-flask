import re

# texto = 'Este coche verde es muy rapido'
# print(texto)
# patron = 'coche'
# encontrado = re.search(patron, texto)
# if encontrado:
#     print(f'patron "{patron}" encontrado')
#     ini = encontrado.start()
#     fin = encontrado.end()
#     print(f'patron "{patron}" empieza en posicion {ini} y termina en {fin}')
# else:
#     print(f'patron "{patron}" no encontrado')

# texto = 'me gusta el color negro y por eso todo lo compro negro'
# patron = 'negro'
# resultado = re.findall(patron, texto)
# print(resultado)
# veces = len(resultado)
# print(veces)

texto = 'me gusta el color negro y por eso todo lo compro negro'
patrones = ['gusta', 'pintura', 'compro']

for patron in patrones:
    print(f'estamos buscando por el patron {patron}')
    resultado = re.findall(patron, texto)
    veces = len(resultado)
    print(veces)
