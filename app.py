from flask import Flask, render_template, flash, request, redirect, url_for
app = Flask(__name__)

#---------------------------------RUTAS ARBOL PRINCIPAL----------------------------------
@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        return render_template('/RAIZ/reservas.html')
    else:
        return render_template('/RAIZ/index.html')

@app.route('/reservas', methods=["GET","POST"])
def reservas():
    return render_template('/RAIZ/reservas.html')

@app.route('/habitacion/<string:id_habitacion>', methods=["GET"])  ####################################
def habitacion(id_habitacion):
    return render_template('/USUARIO/habitacion.html')


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
    if request.method == "POST":
        return render_template('/USUARIO/login.html')
    else:
        return render_template('/USUARIO/registro.html')

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        return render_template('/RAIZ/index.html')
    else:
        return render_template('/USUARIO/login.html')
    

@app.route('/perfil/<string:id_usuario>', methods=["GET"]) 
def perfil(id_usuario):
    return render_template('/USUARIO/perfil.html')  ######

@app.route('/calificar/<string:id_usuario>/<string:id_habitacion>',methods=["GET","POST"])  #### ID USUARIO / ID HABITACION
def calificar(id_usuario,id_habitacion): #VARIABLES
    if request.method == "POST":
        return render_template('/USUARIO/perfil.html')  #VARIABLES
    else:
        return render_template('/USUARIO/calificar.html')  #VARIABLES

"""@app.route('/perfil_reservas', methods=["GET"])
def perfil_reservas():
    return render_template('/USUARIO/perfil_reservas.html')"""

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