from flask import Blueprint,Response,request, make_response, jsonify


from flask import Blueprint, request,make_response,jsonify
from config import logger
from shared.library import library

deletes = Blueprint("deletes", __name__)

@deletes.route('/books', methods=['DELETE'])
def delete_books():
    """Borra un libro por titulo o varios por autor. Uno de los parametros es obligatorio
    ---
    tags:
      - books    
    parameters:
      - in: body
        name: body
        schema:
          id: DeleteBook
          required:
            - author
            - title
          properties:
            author:
              type: string
              description: Autor del libro
              default: Jane Austen
            title:
              type: string
              description: Titulo del libro
              default: Pride and Prejudice   
    definitions:
      StatusResponse:
        type: object
        properties:
          status:
            type: string                 
    responses:
      200:
        description: Libro Borrado. Si el libro no existe se devuelve 200 Ok.
        schema:
          $ref: '#/definitions/StatusResponse'
        examples:
            { "status": "deleted" }
      400:
        description: Libro Borrado
        schema:
          $ref: '#/definitions/StatusResponse'
        examples:
            { "status": "bad request" }            
    """    

    try:
        body = request.json 

        author = body["author"] if "author" in body else None
        title = body["title"] if "title" in body else None

        if author is not None:
            logger.info(f"Borrando libros por autor: {author}")
            books = library.delete_books_by_author(author)
        elif title is not None:
            logger.info(f"Borrando libro por titulo: {title}")
            books = library.delete_book_by_title(title)
        else:
            raise Exception("No se especificó un filtro válido: [author|title]")
        
        library.save_library()

        return make_response({"status": "deleted"}, 200)
    except Exception as e:
        logger.error( str(e) )
        return make_response(jsonify(status="bad request"), 400)