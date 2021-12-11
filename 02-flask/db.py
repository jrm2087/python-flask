from ejemplo7 import db, Persona

db.create_all()

persona1 = Persona('José', 34)
persona2 = Persona('Carolina', 27)

db.session.add_all([persona1, persona2])
db.session.commit()

persona3 = Persona('Darío', 30)
db.session.add(persona3)
db.session.commit()

personas = Persona.query.all()
print('Todas las personas')
print(personas)

filtro1 = Persona.query.filter_by(nombre='José')
print('Filtro por nombre = José')
print(filtro1.all())

select1 = Persona.query.get(1)
print('Busqueda por id')
print(select1)

persona = Persona.query.get(1)
persona.edad = 87
db.session.add(persona)
db.session.commit()

persona_borrar = Persona.query.get(3)
db.session.delete(persona_borrar)
db.session.commit()
print(f'Se ha eliminado persona {persona_borrar}')

personas = Persona.query.all()
print('Todas las personas')
print(personas)
