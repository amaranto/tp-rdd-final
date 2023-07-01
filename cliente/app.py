import requests 
from config import logger

def agregar_libro():
    author = input('''
        Ingrese el autor: ''')
    country = input('''
        Ingrese el pais: ''')
    imageLink = input('''
        Ingrese el link de la imagen: ''')
    language = input('''
        Ingrese el idioma: ''')
    link = input('''
        Ingrese el link: ''')
    pages = input('''
        Ingrese la cantidad de paginas: ''')
    title = input('''
        Ingrese el titulo: ''')
    year = input('''
        Ingrese el año: ''')
    data = {
             "author": author,
             "country": country,
             "imageLink": imageLink,
             "language": language,
             "link": link,
             "pages": int(pages),
             "title": title,
             "year": int(year)
            }
    
    try:
        response = requests.put("http://localhost:5000/books", json=data)
        return response.json()
    except Exception as e:
        
        return {"error": str(e)}
    
def eliminar_libro(author, title):
    try:
        response = requests.delete("http://localhost:5000/books", json={'author': author, 'title': title})
        return response.json()
    except Exception as e:
        
        return {"error": str(e)}
    
def buscar_libro(author: None, title: None, languaje: None, country: None):
    try:
        
        if author is None and title is None and languaje is None and country is None:
            data = {}
        data = {
            'author' : author,
            'title' : title,
            'language' : languaje,
            'country' : country
        }
        response = requests.get("http://localhost:5000/books", params=data)
        return response.json()
    except Exception as e:
        
        return {"error": str(e)}
    
def restaurar_libro():
    try:
        response = requests.post("http://localhost:5000/books/restaurar", json={})
        return response.json()['status']
    except Exception as e:
        
        return {"error": str(e)}
    
def main():

    while True:
        opcion = input('''
        1. Agregar libro
        2. Eliminar libro
        3. Buscar libro
        4. Restaurar base de datos
        5. Salir :> ''')

        if opcion == '1':
            response = agregar_libro()
            
            if "status" not in response or response["status"] != "agregado":
                print(f''' 
                No se pudo agregar el libro ! : {response}
                ''')
            else:
                print('''
                Libro agregado !
                ''')

        elif opcion == '2':
            author = input('''
            - Ingrese el autor: '''
            )    
            title = input('''
            - Ingrese el titulo: '''
            )

            if author == '': author = None
            if title == '': title = None

            response = eliminar_libro(author, title)
            if "status" not in response or response["status"] != "deleted":
                print(f''' 
                No se pudo eliminar el libro ! {response}
                ''')
            else:
                print('''
                Libro eliminado !
                ''')

        elif opcion == '3':
            author = input('''
            - Ingrese el autor: '''
            )

            title = input('''
            - Ingrese el titulo: '''
            )

            languaje = input('''
            - Ingrese el idioma: '''
            )

            country = input('''
            - Ingrese el país: '''
            )

            if author == '': author = None
            if title == '': title = None
            if country == '': country = None
            if languaje == '': languaje = None

            response = buscar_libro(author, title, languaje, country)
            if len(response) == 0:
                print('''
                No se encontraron libros !
                ''')

            for book in response:
                print("====================================")
                for key,value in book.items():
                    print(f"{key}: {value}")
                print("====================================")

        elif opcion == '4':
            response = restaurar_libro()
            print(response)  

        elif opcion == '5':
            logger.info("Adios")
            break
main()