import logging.config
from flask_cors import CORS

import os
from flask import Flask, Blueprint
from smartweb_service import settings
from smartweb_service.api.common.endpoints.common import ns as nodes_user_namespace
from smartweb_service.api.mainchain.endpoints.mainchain import ns as nodes_user_namespace
from smartweb_service.api.sidechain.did.endpoints.sidechain import ns as nodes_user_namespace
from smartweb_service.api.service.mainchain.endpoints.wallet import ns as nodes_user_namespace
from smartweb_service.api.service.sidechain.did.endpoints.did import ns as nodes_user_namespace
from smartweb_service.api.console.endpoints.console import ns as nodes_user_namespace
from smartweb_service.api.hive.endpoints.hive import ns as nodes_user_namespace
from smartweb_service.api.restplus import api
from smartweb_service.database import db

app = Flask(__name__)
CORS(app)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(nodes_user_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)


def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)


if __name__ == "__main__":
    main()
