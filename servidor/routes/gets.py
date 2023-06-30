from flask import Blueprint, request,make_response,jsonify
from config import logger
from models.library import Library

gets = Blueprint("gets", __name__)

@gets.route('/books', methods=['GET'])
def get_books():
    """Ejemplo de endpoint que devuelve una lista de todos los libros o filtrados por autor, titulo, pais o idioma
    ---
    tags:
      - books
    parameters:
      - name: author
        in: path
        type: string        
        required: false
        default: Jane Austen
      - name: title
        in: path
        type: string        
        required: false
        default: Pride and Prejudice
      - name: country
        in: path
        type: string        
        required: false
        default: United Kingdom
      - name: language
        in: path
        type: string        
        required: false
        default: English                        
    responses:
      200:
        description: Biblioteca
        schema:
          type: array
          items:
              $ref: '#/definitions/Book'
          examples:
            [  {
                  "author": "Jane Austen",
                  "country": "United Kingdom",
                  "imageLink": "images/pride-and-prejudice.jpg",
                  "language": "English",
                  "link": "https://en.wikipedia.org/wiki/Pride_and_Prejudice\n",
                  "pages": 226,
                  "title": "Pride and Prejudice",
                  "year": 1813
            }]                
      400:
        description: Error al restaurar DB.
        schema:
          $ref: '#/definitions/StatusResponse'
        examples:
            { "status": "bad request" }                        

    """    
    author = request.args.get('author', default=None, type=str)
    title = request.args.get('title', default=None, type=str)
    country = request.args.get('country', default=None, type=str)
    language = request.args.get('language', default=None, type=str)

    library = Library()
    books = []

    if author is not None:
        books = library.get_books_by_author(author)
        library.set_books(books)
    if title is not None:
        books = library.get_books_by_title(title)
        library.set_books(books)
    if country is not None:
        books = library.get_books_by_country(country)
        library.set_books(books)
    if language is not None:
        books = library.get_books_by_language(language)
        library.set_books(books)
    books = library.get_all_books()

    try:
        return make_response([book.to_json() for book in books], 200)
    except Exception as e:
        logger.error( str(e) )
        return make_response(jsonify(status="bad request"), 400)