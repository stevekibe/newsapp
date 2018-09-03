from flask import Flask
from config import Config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    #creating app configurations
    app.config.from_object(Config_options[config_name])

    # #intializing flask extensionss
    bootstrap.init_app(app)

    #Regestering a blueprint 
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting config
    from .request import configure_request
    configure_request(app)

    return app