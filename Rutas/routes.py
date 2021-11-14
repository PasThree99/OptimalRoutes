#from flask_wtf import form
from wtforms import form
from Rutas import app
from flask import render_template,url_for,redirect
from Rutas.forms import routesForm, newLocationForm, newOrigin
from Rutas.mainAlgorithm import calcularRuta
from Rutas.usefullAlgorithms import deleteSlashes
from Rutas.dbConections import insertNewLocation, updateOrigin


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')


@app.route("/calcular", methods=['POST','GET'])
def calcular_page():
    form2 = routesForm()
    form2.l1.default = '-'
    form2.l2.default = '-'
    form2.l3.default = '-'
    form2.l4.default = '-'
    form2.l5.default = '-'
    form2.l6.default = '-'
    form2.l7.default = '-'
    form2.l8.default = '-'
    form2.l9.default = '-'
    form2.l10.default = '-'
    #form2.process()

    if form2.validate_on_submit():
        global values
        values = []
        values.append(form2.l1.data)
        values.append(form2.l2.data)
        values.append(form2.l3.data)
        values.append(form2.l4.data)
        values.append(form2.l5.data)
        values.append(form2.l6.data)
        values.append(form2.l7.data)
        values.append(form2.l8.data)
        values.append(form2.l9.data)
        values.append(form2.l10.data)
        values = deleteSlashes(values)
        return redirect(url_for('result_page'))

    return render_template('calcular.html', form=form2)

@app.route('/result')
def result_page():
    global values
    res = calcularRuta(values)

    return render_template('result.html', items=res)

@app.route('/cambiar_clave_API')
def cambiar_clave():
    return render_template('cambiarClave.html')


@app.route("/nueva_ubicacion", methods= ["GET","POST"])
def nueva_ubicacion():
    aForm = newLocationForm()
    aForm.l1.default = aForm.l1.label
    aForm.l2.default = aForm.l2.label
    aForm.l3.default = aForm.l3.label

    if(aForm.validate_on_submit()):
        nombre = aForm.l1.data
        latitud = aForm.l2.data
        longitud = aForm.l3.data
        print(nombre,latitud,longitud)
        insertNewLocation(nombre,latitud,longitud)

        return redirect(url_for('insert_exito'))
    return render_template("nueva_ubicacion.html",form =aForm )

@app.route("/exito")
def insert_exito():
    return render_template("newLoc.html")

@app.route("/cambiar_origen",methods= ["GET","POST"])
def cambiar_origen():
    f = newOrigin()
    f.l1.default = f.l1.label

    if(f.validate_on_submit()):
        newLoc = f.l1.data
        updateOrigin(newLoc)
    return render_template("origen_nuevo.html",form = f)

