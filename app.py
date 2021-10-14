from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from forms import RegistroForm, LoginForm, Habitaciones
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)


lista_habitaciones = {
    'id1':{'id':'id1','nombre':'Hab 1', 'descripcion':'Lorem ipsum, dolor sit amet consectetur adipisicing', 'precio':100,'disponible':1, 'imagenes':['img1']},
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
    if request.method == "POST":
        return render_template('zreservas.html')
    else:
        return render_template('index.html', sesion_iniciada=sesion_iniciada)

@app.route('/reservas', methods=["GET","POST"])
def reservas():
    personas = request.args['personas']
    habitaciones = request.args['habitaciones']
    fecha_entrada = request.args['fecha_entrada']
    fecha_salida = request.args['fecha_salida']

    buscar = {'personas':personas, 'habitaciones':habitaciones, 'fecha_entrada':fecha_entrada, 'fecha_salida':fecha_salida}

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

        lista_usuarios[usuario] = {'nombre': nombre,'apellido':apellido,'correo':correo,'password':password}

        return redirect('/login')
    else:
        return render_template('registro.html')

@app.route('/login', methods=["GET","POST"])
def login():
    # form = LoginForm()
    global sesion_iniciada
    if request.method == "POST":
        usuario = request.form['usuario']
        password = request.form['password']
        if usuario in lista_usuarios.keys():
            if password == lista_usuarios[usuario]['password'] :
                sesion_iniciada = True
                return redirect('/')
            else:
                flash("Clave Invalida")
                return redirect("/login")
        elif usuario in correos_admin:
            sesion_iniciada = True
            return render_template("admin_home.html")
        else:
            flash("Usuario Invalido")
            return redirect("/login")
    else:
        return render_template('login.html')

@app.route('/salir', methods=["GET"])
def salir():
    global sesion_iniciada
    sesion_iniciada = False
    return redirect('/')

@app.route('/habitacion/<string:id_habitacion>', methods=["GET"])
def habitacion(id_habitacion):
    global sesion_iniciada
    if id_habitacion in lista_habitaciones.keys():
        
        personas = request.args['personas']
        habitaciones = request.args['habitaciones']
        fecha_entrada = request.args['fecha_entrada']
        fecha_salida = request.args['fecha_salida']

        buscar = {'personas':personas, 'habitaciones':habitaciones, 'fecha_entrada':fecha_entrada, 'fecha_salida':fecha_salida}

        return render_template('habitaciones.html', habitacion=lista_habitaciones[id_habitacion], sesion_iniciada=sesion_iniciada, buscar=buscar, id_habitacion=id_habitacion)
    else:
        return f'habitacion con codigo {id_habitacion} no encontrada'

@app.route('/crear_reserva', methods=["GET","POST"])
def crear_reserva():
    codigo_reserva = "123"
    id_habitacion = request.args['id_habitacion']
    personas = request.args['personas']
    habitaciones = request.args['habitaciones']
    fecha_entrada = request.args['fecha_entrada']
    fecha_salida = request.args['fecha_salida']
    precio = request.args['fecha_salida']

    lista_reservas[codigo_reserva] = {
    'id_user':'andres20',
    'id_habitacion': id_habitacion,
    'personas': personas,
    'habitaciones': habitaciones,
    'fecha_entrada': fecha_entrada,
    'fecha_salida': fecha_salida,
    'valor': precio,
    'dias': 7}

    return "<h3>Reserva generada para habitacion {}, personas: {}, habitaciones {}, fecha_entrada: {} y fecha_salida: {}</h3>".format(id_habitacion, personas, habitaciones, fecha_entrada, fecha_salida)


@app.route('/perfil/<string:id_usuario>', methods=["GET"])
def perfil(id_usuario):
    global sesion_iniciada
    if sesion_iniciada:
        if id_usuario in lista_usuarios.keys():
            return render_template('perfil-cliente.html', id_usuario = id_usuario, lista_reservas=lista_reservas, sesion_iniciada=sesion_iniciada)
        else:
            return f'usuario con codigo {id_usuario} no encontrado'
    else:
        return redirect('/login')

@app.route('/calificar',methods=["GET","POST"])
def calificar():
    if request.method == "POST":
        estrellas = request.form['estrellas']
        mensaje = request.form['mensaje']

        comentarios['id_comentario'] = {
            'estrellas':estrellas,
            'mensaje':mensaje,
            'bloqueo':0
        }

        return redirect('/perfil/Andres')
    else:
        return render_template('calificar.html')

@app.route('/admin_home', methods=["GET","POST"])
def admin_home():
    return render_template('/ADMIN/admin_profile.html')

@app.route('/admin_usuarios', methods=["GET","POST"])
def admin_usuarios():
    return render_template('/ADMIN/admin_gesuser.html')

@app.route('/admin_habitaciones', methods=["GET","POST"])
def admin_habitaciones():
    return render_template('/ADMIN/admin_geshabitacion.html')

@app.route('/agregar_habitacion', methods=["GET","POST"])
def agregar_habitacion():
    form = Habitaciones()
    if request.method == "POST":

        id_habitacion = form.id_habitacion.data
        nombre = form.nombre.data
        descripcion = form.descripcion.data
        precio = form.precio.data

        lista_habitaciones[id_habitacion] = {'nombre':nombre, 'descripcion': descripcion, 'precio': precio, 'imagenes':['img1']}

        return "Habitacion agregada"
    else:
        return render_template('agregar_habitacion.html', form=form)

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