from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Usuario %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email, 
            # do not serialize the password, its a security breach
        }


class Personaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Personaje %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color": self.eye,
            "hair_color": self.hair,
            # do not serialize the password, its a security breach
        }
    
class Planeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Planeta %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            # do not serialize the password, its a security breach
        }


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    crew = db.Column(db.String(250), nullable=False)
    vehicle_class = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Vehicle %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "crew": self.crew,
            "vehicle_class": self.vehicleclass,
            # do not serialize the password, its a security breach
        }



class Personaje_favorito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    personaje_id = db.Column(db.Integer, db.ForeignKey('personaje.id'))
    usuario = db.relationship(Usuario)
    personaje = db.relationship(Personaje)

def __repr__(self):
        return '<Personaje_favorito %r>' % self.id

def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuarioid,
            "personaje_id": self.personajeid,
        }


class Vehicle_favorito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    usuario = db.relationship(Usuario)
    vehicle = db.relationship(Vehicle)

def __repr__(self):
        return '<Vehicle_favorito %r>' % self.id

def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuarioid,
            "vehicle_id": self.vehicleid,
        }


class Planeta_favorito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    planeta_id = db.Column(db.Integer, db.ForeignKey('planeta.id'))
    usuario = db.relationship(Usuario)
    planeta = db.relationship(Planeta)
    
def __repr__(self):
        return '<Vehicle_favorito %r>' % self.id

def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuarioid,
            "planeta_id": self.planetaid,
        }

    