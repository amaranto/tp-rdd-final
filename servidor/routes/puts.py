from flask import Blueprint,Response,request, make_response, jsonify
from config import logger
from shared.library import library
from models.book import Book

puts = Blueprint("puts", __name__)

@puts.route('/books', methods=['PUT'])
def agrega_book():
    """Agrega un libro a la libreria
    ---
    tags:
      - books    
    parameters:
      - in: body
        name: body
        schema:
          id: Book
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
            country:
              type: string
              description: Pais del libro 
              default: United Kingdom
            imageLink:
              type: string
              description: Link de la imagen del libro
              default: http://wikipedia.org/wiki/File:PrideAndPrejudiceTitlePage.jpg
            link:
              type: string
              description: Link del libro
              default: https://en.wikipedia.org/wiki/Pride_and_Prejudice
            language:
              type: string
              description: Idioma del libro
              default: English
            pages:
              type: integer
              description: Cantidad de paginas del libro
              default: 226
            year:
              type: integer
              description: Año de publicacion del libro
              default: 1813
    responses:
      200:
        description: Libro Agregado.
        schema:
          $ref: '#/definitions/StatusResponse'
        examples:
            { "status": "agregado" }
      400:
        description: Error al agregar libro
        schema:
          $ref: '#/definitions/StatusResponse'
        examples:
            { "status": "bad request" }     
    """    

    try:
        body = request.json
        author = body["author"] if "author" in body else None
        title = body["title"] if "title" in body else None
        country = body["country"] if "country" in body else None
        imageLink = body["imageLink"] if "imageLink" in body else None
        link = body["link"] if "link" in body else None
        language = body["language"] if "language" in body else None
        pages =  body["pages"] if "pages" in body else None
        year = body["year"] if "year" in body else None

        book = Book(author, title, country, imageLink, language, link, pages, year)

        print(book.to_json())        
        if author is None or title is None or country is None or imageLink is None or link is None or language is None or pages is None or year is None:
            raise Exception('''Uno o mas parametros no estan completos o son incorrectos. Parametros: [ author: str | title: str | country: str | imageLink: str | link: str | language: str | pages: int | year: int ]''')
        
        library.add_book(book)
        library.save_library()

        return make_response({"status": "agregado"}, 200)
    except Exception as e:
        logger.error( str(e) )
        return make_response(jsonify(status=f"bad request - str({e})"), 400)