from flask import Flask
from flask import render_template, request, redirect, url_for
# from forms import RegistroForm, LoginForm, Habitaciones
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)


lista_habitaciones = {
    'id1':{'id':'id1','nombre':'Hab 1', 'descripcion':'Lorem ipsum, dolor sit amet consectetur adipisicing', 'precio':100,'disponible':1, 'imagenes':['img1']},
    'id2':{'id':'id2','nombre':'Hab 2', 'descripcion':'Lorem ipsum, dolor sit amet consectetur adipisicing', 'precio':200,'disponible':0, 'imagenes':['img1']},
    'id3':{'id':'id3','nombre':'Hab 3', 'descripcion':'Lorem ipsum, dolor sit amet consectetur adipisicing', 'precio':300,'disponible':1, 'imagenes':['img1']}}

lista_usuarios = ['Andres','Carlos','Juan']

lista_reservas = {
    'reserva1': {'id_user':'Andres', 'id_habitacion':'id1', 'valor':1200, 'personas':1,'habitaciones':1,'dias':5},
    'reserva2': {'id_user':'Carlos', 'id_habitacion':'id1', 'valor':1400, 'personas':2,'habitaciones':1,'dias':4},
    'reserva3': {'id_user':'Carlos', 'id_habitacion':'id1', 'valor':1700, 'personas':1,'habitaciones':3,'dias':7},
}

sesion_iniciada = False

@app.route('/', methods=["GET"])
def index():
    if request.method == "POST":
        return render_template('zreservas.html')
    else:
        return render_template('index.html', sesion_iniciada=sesion_iniciada)

@app.route('/reservas', methods=["GET","POST"])
def reservas():
    return render_template('zreservas.html', lista_habitaciones=lista_habitaciones)

@app.route('/registro', methods=["GET","POST"])
def registro():
    # forma = RegistroForm()
    if request.method == "POST":
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        usuario = request.form['usuario']
        password = request.form['password']
        return redirect('/login')
    else:
        return render_template('registro.html')

@app.route('/login', methods=["GET","POST"])
def login():
    # form = LoginForm()
    global sesion_iniciada
    if request.method == "POST":
        correo = request.form['correo']
        password = request.form['password']
        sesion_iniciada = True
        return redirect('/')
    else:
        return render_template('login.html')

@app.route('/salir', methods=["GET"])
def salir():
    global sesion_iniciada
    sesion_iniciada = False
    return redirect('/')

@app.route('/habitacion/<string:id_habitacion>', methods=["GET","POST"])
def habitacion(id_habitacion):
    global sesion_iniciada
    if id_habitacion in lista_habitaciones.keys():
        if request.method == "POST":
            id_habitacion = id_habitacion
            return "Habitacion reservada"
        else:
            return render_template('zhabitacion.html', habitacion=lista_habitaciones[id_habitacion], sesion_iniciada=sesion_iniciada)
    else:
        return f'habitacion con codigo {id_habitacion} no encontrada'

@app.route('/perfil/<string:id_usuario>', methods=["GET"])
def perfil(id_usuario):
    global sesion_iniciada
    if sesion_iniciada:
        if id_usuario in lista_usuarios:
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
        return render_template('zperfil.html')
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
        tipo_habitacion = form.tipo_habitacion.data
        descripcion = form.descripcion.data
        return render_template('index.html')
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

# @app.route('/quienes_somos', methods=["GET"])
# def quienes_somos():
#     return render_template('/RAIZ/quienes_somos.html', methods=["GET"])

# @app.route('/politicas_de_privacidad', methods=["GET"])
# def politicas_de_privacidad():
#     return render_template('/RAIZ/politicas_de_privacidad.html')

# @app.route('/terminos_y_condiciones', methods=["GET"])
# def terminos_y_condiciones():
#     return render_template('/RAIZ/terminos_y_condiciones.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
    # app.run(debug=True)