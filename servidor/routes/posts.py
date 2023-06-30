from flask import Blueprint, make_response, jsonify
from config import logger
from config import BOOKS_SOURCE,   BOOKS_DESTINATION
import requests
import json
from shared.library import library
posts = Blueprint("posts", __name__)

@posts.route('/books/restaurar', methods=['POST'])
def restaurar_libreria():
    """Restaura la libreria a su estado original
    ---        
    tags:
      - books    
    responses:
      200:
        description: Base de datos restaurada.
        schema:
          $ref: '#/definitions/StatusResponse'
        examples:
            { "status": "restaurado" }
      400:
        description: Error al restaurar DB.
        schema:
          $ref: '#/definitions/StatusResponse'
        examples:
            { "status": "bad request" }     
    """    

    try:

        r = requests.get(BOOKS_SOURCE)
        with open(BOOKS_DESTINATION, 'w') as f:
            json.dump(r.json(), f)
        logger.info(f"Se restauro la base de datos: {BOOKS_DESTINATION}")
        with open(BOOKS_DESTINATION, 'r') as f:
            books = json.load(f)
            library.from_json(books)
        logger.info(f"Se cargo la base de datos: {BOOKS_DESTINATION}")
        return make_response({"status": "restaurado"}, 200)
    
    except Exception as e:
        logger.error( str(e) )
        return make_response(jsonify(status=f"bad request - str({e})"), 400)