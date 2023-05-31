"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
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

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

                                # USUARIO

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
    # Usuario = Usuario.query.all()
    user = Usuario.query.filter_by(id=id).first()
    # users_list = list(map(lambda item: item.serialize(),user))
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "result": user.serialize()
    }

    return jsonify(response_body), 200

@app.route('/user', methods=['POST'])
# def create_user():
#     body = json.loads(request.data)
#     # json.loads(request.body.decode(encoding='UTF-8'))
#     print(body)
#     user = User(email=body["email"], password=body["password"], is_active=body["is_active"])
#     db.session.add(user)
#     db.session.commit()

#     response_body = {
#         "msg": "El usuario ha sido creado",
#     }

#     return jsonify(response_body), 200





                                 # PERSONAJE

@app.route('/personaje', methods=['GET'])
def personaje_get():
    results_personaje = Personaje.query.all()
    personaje_list = list(map(lambda item: item.serialize(),results_personaje))
    response_body = {
        "msg": "FUNCIONA PERSONAJES",
        "results": personaje_list
    }
    return jsonify(response_body), 200



@app.route('/personaje/<int:id>', methods=['GET'])
def get_personaje(id):
    personaje = Personaje.query.filter_by(id=id).first()
    # results = Personaje.query.all()
    # personaje_list = list(map(lambda item: item.serialize(),results))
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "result": personaje.serialize()
    }

    return jsonify(response_body), 200



                                        # PLANETA

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
    # results = Planeta.query.all()
    # planeta_list = list(map(lambda item: item.serialize(),results))

    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "result": planeta.serialize()
    }

    return jsonify(response_body), 200



                                    # VEHICLE    

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
    results = Vehicle.query.all()
    vehicle_list = list(map(lambda item: item.serialize(),results))


    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "result": vehicle.serialize()
    }

    return jsonify(response_body), 200




    # PERSONAJE FAVORITO

@app.route('/personaje_favorito', methods=['GET'])
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




    # PLANETA FAVORITO

@app.route('/planeta_favorito', methods=['GET'])
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







    # VEHICLE FAVORITO

@app.route('/vehicle_favorito', methods=['GET'])
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
   

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
