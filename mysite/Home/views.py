from flask import (Blueprint, render_template, redirect, url_for)

home_blueprint = Blueprint('home_blueprint',__name__,template_folder='templates/Home')

@home_blueprint.route('/')
def home():
    return render_template('home.html')