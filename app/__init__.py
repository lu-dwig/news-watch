# from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

def create_app(config_name):
    #app = Flask(__name__,instance_relative_config = True,static_url_path='/static')
    app  = Flask (__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(config_options[config_name])

    # main blueprint configuration 
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .news_request import configure_request
    configure_request(app)

    return app
