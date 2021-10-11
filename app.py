from flask import Flask, render_template, flash, request, redirect, url_for
from forms import RegistroForm
import os

app = Flask(__name__)

app.secret_key= os.urandom(32)

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        return render_template('/RAIZ/reservas.html')
    else:
        return render_template('index.html')

@app.route('/reservas', methods=["GET","POST"])
def reservas():
    return render_template('/RAIZ/reservas.html')

@app.route('/registro', methods=["GET","POST"])
def registro():
    forma = RegistroForm()
    if request.method == "POST":
        nombre = forma.nombre.data
        apellido = forma.apellido.data
        correo = forma.correo.data
        usuario = forma.usuario.data
        contrasena = forma.contrasena.data
        print(nombre, apellido, correo, usuario, contrasena)
        return render_template('registro.html')
    else:
        return render_template('registro.html')

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        return render_template('/RAIZ/index.html')
    else:
        return render_template('/USUARIO/login.html')

@app.route('/habitacion/<string:id_habitacion>', methods=["GET"])
def habitacion(id_habitacion):
    return render_template('/USUARIO/habitacion.html')

@app.route('/perfil/<string:id_usuario>', methods=["GET"]) 
def perfil(id_usuario):
    return render_template('/USUARIO/perfil.html')

@app.route('/calificar',methods=["GET","POST"])
def calificar():
    if request.method == "POST":
        return render_template('/USUARIO/perfil.html')
    else:
        return render_template('calificar.html')

"""@app.route('/perfil_reservas', methods=["GET"])
def perfil_reservas():
    return render_template('/USUARIO/perfil_reservas.html')"""

@app.route('/admin_usuarios', methods=["GET","POST"])
def admin_usuarios():
    return render_template('/ADMIN/admin_gesuser.html')

@app.route('/admin_habitaciones', methods=["GET","POST"])
def admin_habitaciones():
    return render_template('/ADMIN/admin_geshabitacion.html')

@app.route('/admin_comentarios', methods=["GET","POST"])
def admin_comentarios():
    return render_template('/ADMIN/admin_gescomentario.html')

@app.route('/admin_profile', methods=["GET","POST"])
def admin_profile():
    return render_template('/ADMIN/admin_profile.html')

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

@app.route('/superadmin_profile', methods=["GET","POST"])
def superadmin_profile():
    return render_template('/SUPERADMIN/superadmin_profile.html')

@app.route('/quienes_somos', methods=["GET"])
def quienes_somos():
    return render_template('/RAIZ/quienes_somos.html', methods=["GET"])

@app.route('/politicas_de_privacidad', methods=["GET"])
def politicas_de_privacidad():
    return render_template('/RAIZ/politicas_de_privacidad.html')

@app.route('/terminos_y_condiciones', methods=["GET"])
def terminos_y_condiciones():
    return render_template('/RAIZ/terminos_y_condiciones.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
    # app.run(debug=True)