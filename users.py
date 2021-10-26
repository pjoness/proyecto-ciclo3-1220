# from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User():
    def __init__(self, id, nombre, apellido, correo, password, usuario, is_admin=False):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = password
        self.usuario = usuario
        self.is_admin = is_admin

    # def set_password(self, password):
    #     self.password = generate_password_hash(password)

    # def check_password(self, password):
    #     return check_password_hash(self.password, password)

    def to_json(self):
        return {'usuario': self.usuario, 'password': self.password}
    
    def is_active(self):
         return True
    
    def is_anonymous(self):
         return False
    
    def is_authenticated(self):
         return self.authenticated
    
    def get_id(self):
         return self.id

    def __repr__(self):
        return '<User {}>'.format(self.usuario)