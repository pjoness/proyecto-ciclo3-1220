from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from forms import RegistroForm, LoginForm, Habitaciones
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
import os
import db
from users import User
import datetime

app = Flask(__name__)

app.secret_key = os.urandom(32)

login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id_usuario):
    user = db.get_user_by_id(id_usuario)
    return User(id_usuario, user[1], user[2], user[3], user[4], user[5])

bcrypt = Bcrypt(app)


lista_habitaciones = {
    1 :{'id':'id1','nombre':'Hab 1', 'descripcion':'Lorem ipsum, dolor sit amet consectetur adipisicing', 'precio':100,'disponible':1, 'imagenes':['img1']},
    'id2':{'id':'id2','nombre':'Hab 2', 'descripcion':'Lorem ipsum, dolor sit amet consectetur adipisicing', 'precio':200,'disponible':0, 'imagenes':['img1']},
    'id3':{'id':'id3','nombre':'Hab 3', 'descripcion':'Lorem ipsum, dolor sit amet consectetur adipisicing', 'precio':300,'disponible':1, 'imagenes':['img1']}}

lista_usuarios = {
    'andres':{'nombre':'Andres','apellido':'Garcia','correo':'andres@gmail.com','password':'123'},
}

lista_reservas = {
    'reserva1': {'id_user':'Andres', 'id_habitacion':'id1', 'valor':1200, 'personas':1,'habitaciones':1,'dias':5},
    'reserva2': {'id_user':'Carlos', 'id_habitacion':'id1', 'valor':1400, 'personas':2,'habitaciones':1,'dias':4},
    'reserva3': {'id_user':'Carlos', 'id_habitacion':'id1', 'valor':1700, 'personas':1,'habitaciones':3,'dias':7},
}

comentarios = {'1':{'estrellas':5,'mensaje':'Lorem ipsum, dolor sit amet consectetur adipisicing','bloqueo':0}}

sesion_iniciada = False

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html', sesion_iniciada=sesion_iniciada)

@app.route('/reservas', methods=["GET","POST"])
def reservas():
    personas = request.args['personas']
    habitaciones = request.args['habitaciones']
    fecha_entrada = request.args['fecha_entrada']
    fecha_salida = request.args['fecha_salida']

    date_entrada = datetime.datetime.strptime(fecha_entrada, "%Y-%m-%d")
    date_salida = datetime.datetime.strptime(fecha_salida, "%Y-%m-%d")

    dias = (date_salida - date_entrada).days

    lista_habitaciones = db.get_habitaciones()

    buscar = {'personas':personas, 'habitaciones':habitaciones, 'fecha_entrada':fecha_entrada, 'fecha_salida':fecha_salida,
    'dias':dias}

    return render_template('reservas.html', lista_habitaciones=lista_habitaciones, buscar=buscar)

@app.route('/registro', methods=["GET","POST"])
def registro():
    # forma = RegistroForm()
    if request.method == "POST":
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        usuario = request.form['usuario']
        password = request.form['password']

        users = db.get_users()

        if usuario in users:
            flash('Usuario ya existe')
            return render_template('registro.html')
        else:
            lista_usuarios[usuario] = {'nombre': nombre,'apellido':apellido,'correo':correo,'password':password}

            pw_hash = bcrypt.generate_password_hash(password)

            registro = db.add_user(nombre, apellido, correo, pw_hash, usuario, "cliente")

            if registro:
                print("Usuario registrado")

                return redirect('/login')
            else:
                flash("Error en el registro")
                return render_template('registro.html')
    else:
        return render_template('registro.html')

@app.route('/login', methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    
    form = LoginForm()
    global sesion_iniciada
    if request.method == "POST":
        # usuario = request.form['usuario']
        # password = request.form['password']

        usuario = form.usuario.data
        password = form.password.data

        result = db.get_user(usuario)

        isPassword =  bcrypt.check_password_hash(result[4],password)

        if result:
            user = User(int(result[0]), result[1], result[2], result[3], result[4], result[5])

            if usuario == result[5] and isPassword:
                sesion_iniciada = True
                login_user(user, remember = True)
                return redirect('/')
            else:
                flash("Usuario o Clave Invalidos")
                return redirect("/login")                
        else:
            flash("Usuario no existe")
            return redirect("/login")
    else:
        return render_template('login.html', form=form)

@app.route('/salir', methods=["GET"])
def salir():
    global sesion_iniciada
    sesion_iniciada = False
    return redirect('/')

@app.route('/habitacion/<int:id_habitacion>', methods=["GET"])
def habitacion(id_habitacion):
    global sesion_iniciada
    id_habitaciones = db.get_id_habitaciones()
    if id_habitacion in id_habitaciones:
        
        personas = request.args['personas']
        habitaciones = request.args['habitaciones']
        fecha_entrada = request.args['fecha_entrada']
        fecha_salida = request.args['fecha_salida']

        date_entrada = datetime.datetime.strptime(fecha_entrada, "%Y-%m-%d")
        date_salida = datetime.datetime.strptime(fecha_salida, "%Y-%m-%d")

        dias = (date_salida - date_entrada).days

        habitacion = db.get_habitacion(id_habitacion)

        precio = habitacion[3]
        
        valor = precio*dias

        buscar = {'personas':personas, 'habitaciones':habitaciones, 'fecha_entrada':fecha_entrada, 'fecha_salida':fecha_salida,
        'dias':dias,
        'valor':valor}

        return render_template('habitaciones.html', habitacion=habitacion, sesion_iniciada=sesion_iniciada, buscar=buscar, id_habitacion=id_habitacion, valor=valor)
    else:
        return f'habitacion con codigo {id_habitacion} no encontrada'

@app.route('/crear_reserva', methods=["POST"])
@login_required
def crear_reserva():
    id_usuario = "andres20"
    id_habitacion = request.form['id_habitacion']
    personas = request.form['personas']
    habitaciones = request.form['habitaciones']
    fecha_entrada = request.form['fecha_entrada']
    fecha_salida = request.form['fecha_salida']
    dias = request.form['dias']
    valor = request.form['valor']

    reserva = db.add_reserva(id_usuario, personas, habitaciones, fecha_entrada, fecha_salida, dias, valor)

    detalle = db.add_detalle(id_habitacion, valor)

    if reserva:
        return "<p>Reserva generada para habitacion {}, personas: {}, habitaciones {}, fecha_entrada: {} y fecha_salida: {}</p>".format(id_habitacion, personas, habitaciones, fecha_entrada, fecha_salida)
    else:
        flash("Error en la reserva")
        return "<h1>Error en la reserva</h1>"

    return "<p>Reserva generada para habitacion {}, personas: {}, habitaciones {}, fecha_entrada: {} y fecha_salida: {}</p>".format(id_habitacion, personas, habitaciones, fecha_entrada, fecha_salida)


@app.route('/perfil/<string:id_usuario>', methods=["GET"])
@login_required
def perfil(id_usuario):
    global sesion_iniciada
    if sesion_iniciada:
        users = db.get_users()
        if id_usuario in users:
            usuario = db.get_user(id_usuario)
            lista_reservas = db.get_reservas(id_usuario)
            return render_template('perfil-cliente.html', usuario = usuario, lista_reservas=lista_reservas, sesion_iniciada=sesion_iniciada)
        else:
            return f'usuario con codigo {id_usuario} no encontrado'
    else:
        return redirect('/login')

@app.route('/prueba', methods=["GET"])
def prueba():
    return current_user.to_json()


@app.route('/calificar',methods=["GET","POST"])
# @login_required
def calificar():

    codigo = request.args.get('codigo')
    id_usuario = request.args.get('id_usuario')

    if request.method == "POST":
        codigo = request.form['codigo']
        estrellas = request.form['estrellas']
        mensaje = request.form['mensaje']
        id_usuario = request.form['id_usuario']

        comentario = db.add_comentarios(codigo, estrellas, mensaje, id_usuario, 0)

        if comentario:
            print("Comentario creado")
            return redirect('/perfil/andres20')
        else:
            print("Error en comentario")
            return render_template('calificar.html')

        comentarios['id_comentario'] = {
            'estrellas':estrellas,
            'mensaje':mensaje,
            'bloqueo':0
        }

        return redirect('/perfil/Andres')
    else:
        return render_template('calificar.html', codigo=codigo, id_usuario=id_usuario)

@app.route('/admin_home', methods=["GET","POST"])
# @login_required
def admin_home():
    return render_template('perfil-administrador.html')

@app.route('/admin_usuarios', methods=["GET","POST"])
def admin_usuarios():
    return render_template('/ADMIN/admin_gesuser.html')

@app.route('/admin_habitaciones', methods=["GET"])
# @login_required
def admin_habitaciones():
    habitaciones = db.get_habitaciones()
    return render_template('administrador-habitaciones.html', habitaciones=habitaciones)

@app.route('/agregar_habitacion', methods=["GET","POST"])
# @login_required
def agregar_habitacion():
    form = Habitaciones()
    if request.method == "POST":

        id_habitacion = form.id_habitacion.data
        nombre = form.nombre.data
        descripcion = form.descripcion.data
        precio = form.precio.data

        result = db.add_habitacion(nombre, descripcion, precio)

        if result:
            print("Habitacion registrada")
            return render_template('agregar_habitacion.html', form=form)
        else:
            return "<h1>Fallo registro de habitacion</h1>"

        lista_habitaciones[id_habitacion] = {'nombre':nombre, 'descripcion': descripcion, 'precio': precio, 'imagenes':['img1']}

        return "Habitacion agregada"
    else:
        return render_template('agregar_habitacion.html', form=form)

@app.route('/editar_habitacion/<int:id>', methods=["GET","POST"])
# @login_required
def editar_habitacion(id):
    habitacion = db.get_habitacion(id)

    form = Habitaciones()

    form.id_habitacion.data = habitacion[0]
    form.nombre.data = habitacion[1]
    form.descripcion.data = habitacion[2]
    form.precio.data = habitacion[3]

    if request.method == "POST":
        id = request.form['id_habitacion']
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']

        editar = db.editar_habitacion(id,nombre,descripcion,precio)
        
        if editar:
            flash('Habitacion Editada')
            return redirect(url_for('admin_habitaciones'))
        else:
            return "Error"
    else:
        return render_template('editar_habitacion.html', form=form, id=id)

@app.route('/eliminar_habitacion/<int:id>', methods=["POST"])
def eliminar_habitacion(id):
    eliminar = db.eliminar_habitacion(id)
    if eliminar:
        flash('Habitacion Eliminada')
    else:
        flash('Error')
    return redirect(url_for('admin_habitaciones'))

@app.route('/admin_comentarios', methods=["GET","POST"])
def admin_comentarios():
    return render_template('/ADMIN/admin_gescomentario.html')


@app.route('/superadmin_home', methods=["GET","POST"])
def superadmin_home():
    return render_template('/SUPERADMIN/superadmin_profile.html')

@app.route('/superadmin_gesuser', methods=["GET","POST"])
def superadmin_gesuser():
    return render_template('/SUPERADMIN/superadmin_gesuser.html')

@app.route('/superadmin_geshabitacion', methods=["GET","POST"])
def superadmin_geshabitacion():
    return render_template('/SUPERADMIN/superadmin_geshabitacion.html')

@app.route('/superadmin_gescomentario', methods=["GET","POST"])
def superadmin_gescomentario():
    return render_template('/SUPERADMIN/superadmin_gescomentario.html')

@app.route('/superadmin_gesroles', methods=["GET","POST"])
def superadmin_gesroles():
    return render_template('/SUPERADMIN/superadmin_gesroles.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
    # app.run(debug=True)