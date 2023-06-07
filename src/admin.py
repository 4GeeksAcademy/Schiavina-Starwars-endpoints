import os
from flask_admin import Admin
from models import db, Usuario, Personaje, Planeta, Vehicle, Personaje_favorito, Planeta_favorito, Vehicle_favorito
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    class Personaje_favoritoAdmin(ModelView):
        column_list = ("id", "usuario_id", "personaje_id")
        form_columns = ("usuario_id", "personaje_id")
        column_hide_backrefs = False

    class Planeta_favoritoAdmin(ModelView):
        column_list = ("id", "usuario_id", "planeta_id")
        form_columns = ("usuario_id", "planeta_id")
        column_hide_backrefs = False

    class Vehicle_favoritoAdmin(ModelView):
        column_list = ("id", "usuario_id", "vehicle_id")
        form_columns = ("usuario_id", "vehicle_id")
        column_hide_backrefs = False
    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(Usuario, db.session))
    admin.add_view(ModelView(Personaje, db.session))
    admin.add_view(ModelView(Planeta, db.session))
    admin.add_view(ModelView(Vehicle, db.session))
    admin.add_view(Personaje_favoritoAdmin(Personaje_favorito, db.session))
    admin.add_view(Vehicle_favoritoAdmin(Vehicle_favorito, db.session))
    admin.add_view(Planeta_favoritoAdmin(Planeta_favorito, db.session))
    

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))