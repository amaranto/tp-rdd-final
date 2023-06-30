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

    try:
        response = requests.put("http://localhost:5000/books", json={"author": author, "country": country, "imageLink": imageLink, "language": language, "link": link, "pages": int(pages), "title": title, "year": int(year)})
        return response.json()
    except Exception as e:
        
        return {"error": str(e)}
    
def eliminar_libro(param, valor):
    try:
        response = requests.delete("http://localhost:5000/books", json={param: valor})
        return response.json()
    except Exception as e:
        
        return {"error": str(e)}
    
def buscar_libro(param=None, valor=None):
    try:
        data = {} if param is None or valor is None else {param: valor}
        response = requests.get("http://localhost:5000/books", params=data)
        return response.json()
    except Exception as e:
        
        return {"error": str(e)}
    
def restaurar_libro():
    try:
        response = requests.post("http://localhost:5000/books/restaurar", json={})
        return response.json()
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
            param = input('''
            - Ingrese el parametro: '''
            )
            valor = input('''
            - Ingrese el valor: '''
            )
            response = eliminar_libro(param, valor)
            if "status" not in response or response["status"] != "deleted":
                print(f''' 
                No se pudo eliminar el libro ! {response}
                ''')
            else:
                print('''
                Libro eliminado !
                ''')

        elif opcion == '3':
            param = input('''
            - Ingrese el parametro (Enter para ver todos): '''
            )

            valor = None
            if param != '':
                valor = input(
            f'''
            - Ingrese el valor del filtro {param}: '''
            )

            response = buscar_libro(param, valor)
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