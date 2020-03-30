import logging.config
import os
from flask import Flask
from flask_cors import CORS
from flask_restful_swagger_2 import swagger, get_swagger_blueprint
from poetry_demo.views_blueprint import get_user_resources
from poetry_demo import settings


app = Flask(__name__)
CORS(app)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


@app.route('/')
def index():
    return """<head>
    <meta http-equiv="refresh" content="0; url=http://petstore.swagger.io/?url=http://localhost:5000/api/swagger.json" />
    </head>"""


def auth(api_key, endpoint, method):
    # Space for your fancy authentication. Return True if access is granted, otherwise False
    return True


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    docs = []

    swagger.auth = auth
    # Get user resources
    user_resources = get_user_resources()

    # Retrieve and save the swagger document object (do this for each set of resources).
    docs.append(user_resources.get_swagger_doc())

    # Register the blueprint for user resources
    app.register_blueprint(user_resources.blueprint)

    # Prepare a blueprint to server the combined list of swagger document objects and register it
    app.register_blueprint(get_swagger_blueprint(docs, '/api/swagger', title='Example', api_version='1'))


def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)


if __name__ == "__main__":
    main()
