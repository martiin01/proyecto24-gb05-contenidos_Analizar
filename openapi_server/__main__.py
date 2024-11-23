import connexion
from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from openapi_server import encoder
from openapi_server.databaseContenido import Contenido





def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml', arguments={'title': 'Contenidos API'}, pythonic_params=True)
    app.run(port=8080)

if __name__ == '__main__':
    main()
