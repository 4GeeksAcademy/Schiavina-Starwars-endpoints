"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import json
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Usuario, Personaje, Planeta, Vehicle, Personaje_favorito, Planeta_favorito, Vehicle_favorito
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)



# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#############################################################
#########################USUARIO#############################
#############################################################

@app.route('/usuario', methods=['GET'])
def usuario_get():
    results = Usuario.query.all()
    users_list = list(map(lambda item: item.serialize(),results))
    
    response_body = {
        "msg": "Hello, this is your GET /usuario response ",
        "results": users_list
    }
    return jsonify(response_body), 200


@app.route('/usuario/<int:id>', methods=['GET'])
def get_user(id):
    user = Usuario.query.filter_by(id=id).first()
    if user is None:
        raise APIException("No hay un usuario con ese ID", status_code=404)
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "result": user.serialize()
    }

    return jsonify(response_body), 200

@app.route('/usuario', methods=['POST'])
def create_user():
    body = json.loads(request.data)
    user = Usuario(email=body["email"], password=body["password"], name=body["name"])
    db.session.add(user)
    db.session.commit()
    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)
    if 'email' not in body:
        raise APIException('Te falta añadir un correo electrónico', status_code=400)
    if 'password' not in body:
        raise APIException('Te falta añadir una contraseña', status_code=400)
    if 'name' not in body:
        raise APIException('Te falta añadir una nombre', status_code=400)

    response_body = {
        "msg": "El usuario ha sido creado",
    }

    return jsonify(response_body), 200


@app.route('/usuario/<int:id>', methods=['DELETE'])
def delete_user(id):
    print(id)

    user = Usuario.query.filter_by(id=id).first()
    if user is None:
        raise APIException("No hay un usuario con ese ID", status_code=404)

    db.session.delete(user)
    db.session.commit()

    response_body = {
        "msg": "El usuario ha sido borrado",
    }

    return jsonify(response_body), 200




#############################################################
#########################PERSONAJE#############################
#############################################################

@app.route('/personaje', methods=['GET'])
def personaje_get():
    results_personaje = Personaje.query.all()
    personaje_list = list(map(lambda item: item.serialize(),results_personaje))
    print("OK")
    response_body = {
        "msg": "FUNCIONA PERSONAJES",
        "results": personaje_list
    }
    return jsonify(response_body), 200



@app.route('/personaje/<int:id>', methods=['GET'])
def get_personaje(id):
    personaje = Personaje.query.filter_by(id=id).first()

    if personaje is None:
        raise APIException("No hay un personaje con ese ID", status_code=404)
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "result": personaje.serialize()
    }

    return jsonify(response_body), 200


@app.route('/personaje', methods=['POST'])
def create_personaje():
    body = json.loads(request.data)
    personaje = Personaje(eye_color=body["eye_color"], hair_color=body["hair_color"], name=body["name"])
    db.session.add(personaje)
    db.session.commit()
    response_body = {
        "msg": "El Personaje ha sido creado",
    }

    return jsonify(response_body), 200

@app.route('/personaje/<int:id>', methods=['DELETE'])
def delete_personaje(id):
    print(id)

    personaje = Personaje.query.filter_by(id=id).first()
    if personaje is None:
        raise APIException("No hay un personaje con ese ID", status_code=404)

    db.session.delete(personaje)
    db.session.commit()

    response_body = {
        "msg": "El personaje ha sido borrado",
    }

    return jsonify(response_body), 200

#############################################################
#########################PLANETA#############################
#############################################################

@app.route('/planeta', methods=['GET'])
def handle_planeta():
    results = Planeta.query.all()
    planeta_list = list(map(lambda item: item.serialize(),results))
    
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "result": planeta_list
    }
    return jsonify(response_body), 200
    

@app.route('/planeta/<int:id>', methods=['GET'])
def get_planeta(id):
    planeta = Planeta.query.filter_by(id=id).first()
    if planeta is None:
        raise APIException("No hay un planeta con ese ID", status_code=404)
 

    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "result": planeta.serialize()
    }

    return jsonify(response_body), 200



@app.route('/planeta', methods=['POST'])
def create_planeta():
    body = json.loads(request.data)
    planeta = Planeta(name=body["name"], population=body["population"], terrain=body["terrain"])
    db.session.add(planeta)
    db.session.commit()
    response_body = {
        "msg": "El Planeta ha sido creado",
    }

    return jsonify(response_body), 200



@app.route('/planeta/<int:id>', methods=['DELETE'])
def delete_planeta(id):
    print(id)

    planeta = Planeta.query.filter_by(id=id).first()
    if planeta is None:
        raise APIException("No hay un planeta con ese ID", status_code=404)

    db.session.delete(planeta)
    db.session.commit()

    response_body = {
        "msg": "El planeta ha sido borrado",
    }

    return jsonify(response_body), 200



#############################################################
#########################VEHICLE#############################
############################################################# 

@app.route('/vehicle', methods=['GET'])
def vehicle_get():
    results_vehicle = Vehicle.query.all()
    vehicle_list = list(map(lambda item: item.serialize(),results_vehicle))
    response_body = {
        "msg": "FUNCIONA PLANETA",
        "results": vehicle_list
    }
    return jsonify(response_body), 200

@app.route('/vehicle/<int:id>', methods=['GET'])
def get_vehicle(id):
    vehicle = Vehicle.query.filter_by(id=id).first()
    if vehicle is None:
        raise APIException("No hay un vehiculo con ese ID", status_code=404)

    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "result": vehicle.serialize()
    }

    return jsonify(response_body), 200


@app.route('/vehicle', methods=['POST'])
def create_vehicle():
    body = json.loads(request.data)
    vehicle = Vehicle(crew=body["crew"], name=body["name"], vehicle_class=body["vehicle_class"])
    db.session.add(vehicle)
    db.session.commit()
    response_body = {
        "msg": "El Vehiculo ha sido creado",
    }

    return jsonify(response_body), 200


@app.route('/vehicle/<int:id>', methods=['DELETE'])
def delete_vehicle(id):
    print(id)

    vehicle = Vehicle.query.filter_by(id=id).first()
    if vehicle is None:
        raise APIException("No hay un vehiculo con ese ID", status_code=404)

    db.session.delete(vehicle)
    db.session.commit()

    response_body = {
        "msg": "El vehiculo ha sido borrado",
    }

    return jsonify(response_body), 200



#############################################################
#########################PERSONAJE FAVORITO#############################
#############################################################

@app.route('/personaje_favorito', methods=['GET'])
# @jwt_required()
def personajefav_get():
    results = Personaje_favorito.query.all()
    personaje_favorito_list = list(map(lambda item: item.serialize(),results))
    print(results)
    response_body = {
        "msg": "FUNCIONA PERSONAJES_FAVORITOS",
        "results": personaje_favorito_list
    }
    return jsonify(response_body), 200



@app.route('/personaje_favorito/<int:id>', methods=['GET'])
def get_personajefav(id):
    personajefav = Personaje_favorito.query.filter_by(id=id).first()

    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "result": personajefav.serialize()
    }

    return jsonify(response_body), 200

@app.route('/personaje_favorito', methods=['POST'])
def create_personajefav():
    body = json.loads(request.data)
    personajefav = Personaje_favorito(usuario_id=body["usuario_id"], personaje_id=body["personaje_id"])
    db.session.add(personajefav)
    db.session.commit()
    response_body = {
        "msg": "El Personaje favorito ha sido creado",
    }

    return jsonify(response_body), 200



@app.route('/personaje_favorito/<int:id>', methods=['DELETE'])
def delete_personajefav(id):
    personaje = Personaje_favorito.query.get(id)
    if Personaje_favorito is None:
        raise APIException('Favorito not found', status_code=404)
    db.session.delete(personaje)
    db.session.commit()
    response_body = {
        "msg": "Personaje favorito eliminado",
    }

    return jsonify(response_body), 200




#############################################################
#########################PLANETA FAVORITO#############################
#############################################################

@app.route('/planeta_favorito', methods=['GET'])
# @jwt_required()
def planetafav_get():
    results = Planeta_favorito.query.all()
    planeta_favorito_list = list(map(lambda item: item.serialize(),results))
    response_body = {
        "msg": "FUNCIONA PLANETA_FAVORITOS",
        "results": planeta_favorito_list
    }
    return jsonify(response_body), 200


@app.route('/planeta_favorito/<int:id>', methods=['GET'])
def get_planetafav(id):
    planetafav = Planeta_favorito.query.filter_by(id=id).first()
    
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "result": planetafav.serialize()
    }

    return jsonify(response_body), 200


@app.route('/planeta_favorito', methods=['POST'])
def create_planetafav():
    body = json.loads(request.data)
    planetafav = Planeta_favorito(usuario_id=body["usuario_id"], planeta_id=body["planeta_id"])
    db.session.add(planetafav)
    db.session.commit()
    response_body = {
        "msg": "El Planeta favorito ha sido creado",
    }

    return jsonify(response_body), 200



@app.route('/planeta_favorito/<int:id>', methods=['DELETE'])
def delete_planetafav(id):
    planeta = Planeta_favorito.query.get(id)
    if Planeta_favorito is None:
        raise APIException('Favorito not found', status_code=404)
    db.session.delete(planeta)
    db.session.commit()
    response_body = {
        "msg": "Planeta favorito eliminado",
    }

    return jsonify(response_body), 200




#############################################################
#########################VEHICLE FAVORITO#############################
#############################################################

@app.route('/vehicle_favorito', methods=['GET'])
# @jwt_required()
def vehiclefav_get():
    results = Vehicle_favorito.query.all()
    vehicle_favorito_list = list(map(lambda item: item.serialize(),results))
    response_body = {
        "msg": "FUNCIONA VEHICLE_FAVORITOS",
        "results": vehicle_favorito_list
    }
    return jsonify(response_body), 200



@app.route('/vehicle_favorito/<int:id>', methods=['GET'])
def get_vehiclefav(id):
    vehiclefav = Vehicle_favorito.query.filter_by(id=id).first()
    
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "result": vehiclefav.serialize()
    }

    return jsonify(response_body), 200



@app.route('/vehicle_favorito', methods=['POST'])
def create_vehiclefav():
    body = json.loads(request.data)
    vehiclefav = Vehicle_favorito(usuario_id=body["usuario_id"], vehicle_id=body["vehicle_id"])
    db.session.add(vehiclefav)
    db.session.commit()
    response_body = {
        "msg": "El Vehiculo favorito ha sido creado",
    }

    return jsonify(response_body), 200



@app.route('/vehicle_favorito/<int:id>', methods=['DELETE'])
def delete_vehiclefav(id):
    vehicle = Vehicle_favorito.query.get(id)
    if Vehicle_favorito is None:
        raise APIException('Favorito not found', status_code=404)
    db.session.delete(vehicle)
    db.session.commit()
    response_body = {
        "msg": "Vehicle favorito eliminado",
    }

    return jsonify(response_body), 200







 
 #############################################################
#########################LOGIN#############################
#############################################################
@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user = Usuario.query.filter_by(email=email).first()
    # print(user.email)
    if user is None: 
        return jsonify({"msg": "No existe"}), 404
    if email != user.email or password != user.password:
        return jsonify({"msg": "bad email or password"}), 401
    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)







   

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)



@app.route("/profile", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


if __name__ == "__main__":
    app.run()
