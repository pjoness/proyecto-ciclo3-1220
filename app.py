from flask import Flask, render_template, flash, request, redirect, url_for

app = Flask(__name__)

#---------------------------------RUTAS ARBOL PRINCIPAL----------------------------------
@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
      return render_template("/RAIZ/reservas.html")
    return render_template('/RAIZ/index.html')

@app.route('/reservas', methods=["GET","POST"])
def reservas():
    return render_template('/RAIZ/reservas.html')

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
    return render_template('/USUARIO/registro.html')

@app.route('/habitacion/<string:id_habitacion>', methods=["GET"])
def habitacion():
    return render_template('/USUARIO/habitacion.html')

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
      return redirect("/RAIZ/index")
    return render_template('/USUARIO/login.html')

@app.route('/perfil/<string:id_usuario>', methods=["GET"])
def perfil():
    return render_template('/USUARIO/perfil.html')

@app.route('/perfil_reservas', methods=["GET"])
def perfil_reservas():
    return render_template('/USUARIO/perfil_reservas.html')

#---------------------------------RUTAS ADMINISTRADOR----------------------------------
@app.route('/admin_gesuser', methods=["GET"])
def admin_gesuser():
    return render_template('/ADMIN/admin_gesuser.html')

@app.route('/admin_geshabitacion', methods=["GET"])
def admin_geshabitacion():
    return render_template('/ADMIN/admin_geshabitacion.html')

@app.route('/admin_gescomentario', methods=["GET"])
def admin_gescomentario():
    return render_template('/ADMIN/admin_gescomentario.html')

@app.route('/admin_profile', methods=["GET"])
def admin_profile():
    return render_template('/ADMIN/admin_profile.html')

#---------------------------------RUTAS SUPER ADMINISTRADOR----------------------------------
@app.route('/superadmin_gesuser', methods=["GET"])
def superadmin_gesuser():
    return render_template('/SUPERADMIN/superadmin_gesuser.html')

@app.route('/superadmin_geshabitacion', methods=["GET"])
def superadmin_geshabitacion():
    return render_template('/SUPERADMIN/superadmin_geshabitacion.html')

@app.route('/superadmin_gescomentario', methods=["GET"])
def superadmin_gescomentario():
    return render_template('/SUPERADMIN/superadmin_gescomentario.html')

@app.route('/superadmin_gesroles', methods=["GET"])
def superadmin_gesroles():
    return render_template('/SUPERADMIN/superadmin_gesroles.html')

@app.route('/superadmin_profile', methods=["GET"])
def superadmin_profile():
    return render_template('/SUPERADMIN/superadmin_profile.html')

if __name__=='__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5001, debug=True)