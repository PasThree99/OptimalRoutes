from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.fields.core import FloatField
from wtforms.fields.simple import TextField
from Rutas.dbConections import getAllPlaces
from Rutas.usefullAlgorithms import listOfTuples

class routesForm(FlaskForm):
    op = [('-','-')]
    op.extend(listOfTuples(getAllPlaces()))


    l1 = SelectField(label = "Lugar 1", choices=op)
    l2 = SelectField(label = "Lugar 2", choices=op)
    l3 = SelectField(label = "Lugar 3", choices=op)
    l4 = SelectField(label = "Lugar 4", choices=op)
    l5 = SelectField(label = "Lugar 5", choices=op)
    l6 = SelectField(label = "Lugar 6", choices=op)
    l7 = SelectField(label = "Lugar 7", choices=op)
    l8 = SelectField(label = "Lugar 8", choices=op)
    l9 = SelectField(label = "Lugar 9", choices=op)
    l10 = SelectField(label = "Lugar 10", choices=op)
    s = SubmitField(label='Submit')

class newLocationForm(FlaskForm):
    l1 = TextField(label="Nombre")
    l2 = FloatField(label = "Latitud")
    l3 =  FloatField(label="Longitud")
    s = SubmitField(label='Submit')
    
class newOrigin(FlaskForm):
    op = [('-','-')]
    op.extend(listOfTuples(getAllPlaces()))
    l1 = SelectField(label = "Lugar 1", choices=op)
    s = SubmitField(label='Submit')