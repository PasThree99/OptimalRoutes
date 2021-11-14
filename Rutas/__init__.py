from flask import Flask, render_template,url_for
app = Flask(__name__)
app.config['SECRET_KEY'] = '1f9b3dbffaaf9eff399efd93'

from Rutas import routes 