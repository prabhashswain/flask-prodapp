try:
    import os
    from flask import Flask
    from flask import (Flask, request,
                       render_template
                       )
    from flask_sqlalchemy import SQLAlchemy
except Exception as e:
    print("Some Modules are Missing {}".format(e))

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config["SECRET_KEY"] = "mysecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(BASE_DIR,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from mysite.Home.views import home_blueprint
app.register_blueprint(home_blueprint,url_prefix='/home')