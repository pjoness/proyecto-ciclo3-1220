from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField 

class FormInicio(FlaskForm):

    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacío, completar')])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacío, completar')])
    recordar = BooleanField('Recordar Usuario')
    enviar = SubmitField('Iniciar Sesión')

class FormRegistro(FlaskForm):

    nombre = StringField('Nombre', validators=[DataRequired(message='No dejar vacío, completar')])
    apellido = StringField('Apellido', validators=[DataRequired(message='No dejar vacío, completar')])
    correo = EmailField('Correo', validators=[DataRequired(message='No dejar vacío, completar'),Email()])
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacío, completar')])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacío, completar')])
    enviar = SubmitField('Iniciar Sesión')

class FormCalificar(FlaskForm):
    comentario = StringField('Comentario', validators=[DataRequired(message='No dejar vacío, completar')])
    enviar = SubmitField('Enviar')

#---------------------------------------------POR ADICIONAR FORMULARIOS--------------------------------    
class BuscarForm(FlaskForm):
    personas = StringField('personas', DataRequired())
    habitaciones = StringField('habitaciones', DataRequired())
    fecha_entrada = DateField('fecha_entrada', DataRequired())
    fecha_salida = DateField('fecha_salida', DataRequired())
    buscar = SubmitField('buscar')

class BuscarUsuariosForm(FlaskForm):
    id_usuario = StringField('id_usuario')
    buscar = SubmitField('buscar')

class BuscarHabitacionesForm(FlaskForm):
    id_habitacion = StringField('id_habitacion')
    buscar = SubmitField('buscar')

class BuscarComentariosForm(FlaskForm):
    id_comentario = StringField('id_comentario')
    buscar = SubmitField('buscar')

class AdminUsuariosForm(FlaskForm):
    id_usuario = StringField('id_usuario')
    nombre = StringField('nombre', validators=[DataRequired(message='No dejar vacío, completar')])
    apellido = StringField('apellido', validators=[DataRequired(message='No dejar vacío, completar')])
    correo = StringField('correo', validators=[DataRequired(message='No dejar vacío, completar'), Email()])
    usuario = StringField('usuario', validators=[DataRequired(message='No dejar vacío, completar')])
    contraseña = PasswordField('contraseña', validators=[DataRequired(message='No dejar vacío, completar')])
    crear = SubmitField('crear')
    editar = SubmitField('editar')
    eliminar = SubmitField('eliminar')

class AdminHabitacionesForm(FlaskForm):
    id_habitacion = StringField('id_habitacion')
    tipo_habitacion = StringField('tipo_habitacion', DataRequired())
    descripcion = TextAreaField('descripcion', DataRequired())
    crear = SubmitField('crear')
    editar = SubmitField('editar')
    eliminar = SubmitField('eliminar')

class AdminComentariosForm(FlaskForm):
    id_comentario = StringField('id_comentario')
    bloquear = SubmitField('bloquear')