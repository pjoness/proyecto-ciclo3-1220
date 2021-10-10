from flask import Flask, render_template, flash, request, url_for
from forms import FormCalificar, FormInicio, FormRegistro
import os
from werkzeug.utils import redirect


app = Flask(__name__)
app.secret_key= os.urandom(24)

lista_habitaciones={
    1 : {"titulo" : "Habitacion 1", "cuerpo":"Descripcion 1", "imagenes":["img 1","img 2"]}, 
    2 : {"titulo" : "Habitacion 2", "cuerpo":"Descripcion 2", "imagenes":["img 1","img 2"]}, 
    3 : {"titulo" : "Habitacion 3", "cuerpo":"Descripcion 3", "imagenes":["img 1","img 2"]}, 
    4 : {"titulo" : "Habitacion 4", "cuerpo":"Descripcion 4", "imagenes":["img 1","img 2"]}, 
    5 : {"titulo" : "Habitacion 5", "cuerpo":"Descripcion 5", "imagenes":["img 1","img 2"]}, 
    6 : {"titulo" : "Habitacion 6", "cuerpo":"Descripcion 6", "imagenes":["img 1","img 2"]}, 
    7 : {"titulo" : "Habitacion 7", "cuerpo":"Descripcion 7", "imagenes":["img 1","img 2"]}, 
}

#---------------------------------RUTAS ARBOL PRINCIPAL----------------------------------
@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        return render_template('/RAIZ/reservas.html')
    else:
        return render_template('/RAIZ/index.html',lista_habitaciones=lista_habitaciones)

@app.route('/reservas', methods=["GET","POST"])
def reservas():
    return render_template('/RAIZ/reservas.html')

@app.route('/habitacion/<int:id_habitacion>', methods=["GET"])
def habitacion(id_habitacion):
    if id_habitacion==1:
        return render_template('/USUARIO/habitaciones/habitacion1.html')
    elif id_habitacion==2:
        return render_template('/USUARIO/habitaciones/habitacion2.html')
    elif id_habitacion==3:
        return render_template('/USUARIO/habitaciones/habitacion3.html')
    elif id_habitacion==4:
        return render_template('/USUARIO/habitaciones/habitacion4.html')
    elif id_habitacion==5:
        return render_template('/USUARIO/habitaciones/habitacion5.html')
    elif id_habitacion==6:
        return render_template('/USUARIO/habitaciones/habitacion6.html')
    elif id_habitacion==7:
        return render_template('/USUARIO/habitaciones/habitacion7.html')
    else:
        return render_template('/USUARIO/habitaciones/no_encontrado.html')


@app.route('/quienes_somos', methods=["GET"])
def quienes_somos():
    return render_template('/RAIZ/quienes_somos.html', methods=["GET"])

@app.route('/politicas_de_privacidad', methods=["GET"])
def politicas_de_privacidad():
    return render_template('/RAIZ/politicas_de_privacidad.html')

@app.route('/terminos_y_condiciones', methods=["GET"])
def terminos_y_condiciones():
    return render_template('/RAIZ/terminos_y_condiciones.html')

#---------------------------------RUTAS ESPECIFICAS DE USUARIO----------------------------------
@app.route('/registro', methods=["GET","POST"])
def registro():
    formulario=FormRegistro()
    if request.method == "POST":
        return redirect("/login")
    else:
        return render_template('/USUARIO/registro.html',form=formulario)

@app.route('/login', methods=["GET","POST"])
def login():
    formulario=FormInicio()
    if request.method == "POST":
        return redirect("/login")
    else:
        return render_template('/USUARIO/login.html',form=formulario)
    

@app.route('/perfil/<string:id_usuario>', methods=["GET"]) 
def perfil(id_usuario):
    return render_template('/USUARIO/perfil.html',name=id_usuario)


@app.route('/calificar/<string:id_usuario>/<string:id_habitacion>', methods=["GET","POST"])
def calificar(id_usuario,id_habitacion):
    formulario=FormCalificar()
    if  request.method == "post":
        return render_template('/USUARIO/perfil.html',name=id_usuario) 
    else:
        return render_template('/USUARIO/calificar.html', id_user=id_usuario, id_room=id_habitacion,form=formulario)  #VARIABLES

#---------------------------------RUTAS ADMINISTRADOR----------------------------------
@app.route('/admin_gesuser', methods=["GET","POST"])
def admin_gesuser():
    return render_template('/ADMIN/admin_gesuser.html')

@app.route('/admin_geshabitacion', methods=["GET","POST"])
def admin_geshabitacion():
    return render_template('/ADMIN/admin_geshabitacion.html')

@app.route('/admin_gescomentario', methods=["GET","POST"])
def admin_gescomentario():
    return render_template('/ADMIN/admin_gescomentario.html')

@app.route('/admin_profile', methods=["GET","POST"])
def admin_profile():
    return render_template('/ADMIN/admin_profile.html')

#---------------------------------RUTAS SUPER ADMINISTRADOR----------------------------------
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


if __name__=='__main__':
    app.run(debug=True)