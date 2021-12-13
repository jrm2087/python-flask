from ejemplo8 import db, Mascota, Juguete, Propietario

mascota1 = Mascota('Maya')
mascota2 = Mascota('Canela')

db.session.add_all([mascota1, mascota2])
db.session.commit()

mascotas = Mascota.query.all()
print(mascotas)

mascota1 = Mascota.query.filter_by(nombre='Maya').first()

propietario1 = Propietario('José', mascota1.id)
db.session.add(propietario1)
db.session.commit()

juguete1 = Juguete('Pelota', mascota1.id)
juguete2 = Juguete('Peluche', mascota1.id)
db.session.add_all([juguete1, juguete2])
db.session.commit()

mascota = Mascota.query.filter_by(nombre='Maya').first()
print(mascota)
mascota.mostrar_juguetes()
