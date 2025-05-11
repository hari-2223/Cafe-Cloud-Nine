#import flask - from package import class
from flask import Flask, render_template, session
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

#create function that creates a web application

def create_app():
    app.debug = True
    app.secret_key = 'Defaultsecretkey'

    bootstrap = Bootstrap5(app)
    
    #importing modules here to avoid circular references, register blueprints of routes
    from . import views
    app.register_blueprint(views.bp)
    from . import session

    return app