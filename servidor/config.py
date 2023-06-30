
import sys
from pathlib import Path
from os import getenv
 
sys.path.append(str(Path(__file__).parent.parent.absolute()))
from tools.logger import DEBUG_LEVEL,logger

logger = logger
DEBUG_LEVEL = DEBUG_LEVEL
ENVIRONMENT = getenv("ENVIRONMENT", "develop")
ALLOWED_HOST= getenv("ALLOWED_HOST", "0.0.0.0")
BOOKS_SOURCE = getenv("BOOKS_SOURCE", "https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json")
BOOKS_DESTINATION = getenv("BOOKS_DESTINATION", "books.json")
PORT =  getenv("PORT", "5000")
SWAGGER_CONFIG = swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/tp-server.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}
