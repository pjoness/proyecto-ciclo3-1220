from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired#, Email

class RegistroForm(FlaskForm):
    nombre = StringField('nombre', validators=[DataRequired(message='No dejar vacío, completar')])

    apellido = StringField('apellido', validators=[DataRequired(message='No dejar vacío, completar')])

    correo = StringField('correo', validators=[DataRequired(message='No dejar vacío, completar')])

    usuario = StringField('usuario', validators=[DataRequired(message='No dejar vacío, completar')])

    contrasena = PasswordField('contraseña', validators=[DataRequired(message='No dejar vacío, completar')])

    crear_cuenta = SubmitField('crear_cuenta')

class LoginForm(FlaskForm):
    correo = StringField('correo', validators=[DataRequired(message='No dejar vacío, completar')])
    
    contraseña = PasswordField('contraseña', validators=[DataRequired(message='No dejar vacío, completar')])

    iniciar_sesion = SubmitField('iniciar_sesion')

class BuscarForm(FlaskForm):
    personas = StringField('personas', DataRequired())

    habitaciones = StringField('habitaciones', DataRequired())

    fecha_entrada = DateField('fecha_entrada', DataRequired())

    fecha_salida = DateField('fecha_salida', DataRequired())
  
    buscar = SubmitField('buscar')

class CalificacionForm(FlaskForm):
    estrellas = StringField('estrellas', DataRequired())

    mensaje = TextAreaField('mensaje')

    enviar = SubmitField('enviar')

class BuscarUsuariosForm(FlaskForm):
    id_usuario = StringField('id_usuario')

    buscar = SubmitField('buscar')

class BuscarHabitacionesForm(FlaskForm):
    id_habitacion = StringField('id_habitacion')

    buscar = SubmitField('buscar')

class BuscarComentariosForm(FlaskForm):
    id_comentario = StringField('id_comentario')

    buscar = SubmitField('buscar')

class Usuarios(FlaskForm):
    id_usuario = StringField('id_usuario')

    nombre = StringField('nombre', validators=[DataRequired(message='No dejar vacío, completar')])

    apellido = StringField('apellido', validators=[DataRequired(message='No dejar vacío, completar')])

    correo = StringField('correo', validators=[DataRequired(message='No dejar vacío, completar')])

    usuario = StringField('usuario', validators=[DataRequired(message='No dejar vacío, completar')])

    contraseña = PasswordField('contraseña', validators=[DataRequired(message='No dejar vacío, completar')])

    crear = SubmitField('crear')
    editar = SubmitField('editar')
    eliminar = SubmitField('eliminar')

class Habitaciones(FlaskForm):
    id_habitacion = StringField('id_habitacion')

    tipo_habitacion = StringField('tipo_habitacion', DataRequired())

    descripcion = TextAreaField('descripcion', DataRequired())

    crear = SubmitField('crear')
    editar = SubmitField('editar')
    eliminar = SubmitField('eliminar')

class Comentarios(FlaskForm):
    id_comentario = StringField('id_comentario')

    bloquear = SubmitField('bloquear')

# class FormInicio(FlaskForm):
#     usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacío, completar')])

#     contraseña = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacío, completar')])

#     recordar = BooleanField('Recordar Usuario')
#     enviar = SubmitField('Iniciar Sesión')