import requests
import os.path
import json
import traceback
from flask import Flask
from flasgger import Swagger

from config import logger, ALLOWED_HOST,PORT, BOOKS_SOURCE, BOOKS_DESTINATION, DEBUG_LEVEL, SWAGGER_CONFIG
from shared.library import library

from routes.gets import gets
from routes.puts import puts
from routes.posts import posts
from routes.deletes import deletes

def download_db():
    try:
        if os.path.isfile(BOOKS_DESTINATION) :
            logger.info(f"La base de datos ya existe: {BOOKS_DESTINATION}")
            return None 
        else:
            r = requests.get(BOOKS_SOURCE)
            with open(BOOKS_DESTINATION, 'w') as f:
                json.dump(r.json(), f)
            logger.info(f"Se descargo la base de datos: {BOOKS_SOURCE}")
    except Exception as e:
        traceback.print_exc()
        logger.error( f"No se puede descargar la base de datos: {BOOKS_SOURCE}")
        logger.error( f"Error: {str(e)}")

def load_db():
    try:
        with open(BOOKS_DESTINATION, 'r') as f:
            
            books = json.load(f)
           

        logger.info(f"Se cargo la base de datos: {BOOKS_DESTINATION}")
        return library.from_json(books)
    
    except Exception as e:
        traceback.print_exc()
        logger.error( f"No se puede cargar la base de datos: {BOOKS_DESTINATION}")
        logger.error( f"Error: {str(e)}")
        return None
    
def create_app():


    app = Flask(__name__)

    app.secret_key = 'secret-key'

    app.register_blueprint(gets)
    app.register_blueprint(puts)
    app.register_blueprint(posts)
    app.register_blueprint(deletes)
    return app

download_db()
load_db()
t = create_app()
swagger = Swagger(t, config=SWAGGER_CONFIG)

t.run(host=ALLOWED_HOST, port=PORT, debug=DEBUG_LEVEL)

