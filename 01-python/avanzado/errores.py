# tratamiento de errores

try:
    fichero = open('datos3.txt', 'r')
    fichero.write('datos para el archivo')
    fichero.close()
except IOError:
    print('error IOError')
except:
    print('error general')
else:
    print('tratando el fichero correcto')
finally:
    print('finalizado tratamiento del fichero')

print('continua')
