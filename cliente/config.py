
import sys
from pathlib import Path
from os import getenv
 
sys.path.append(str(Path(__file__).parent.parent.absolute()))
from tools.logger import DEBUG_LEVEL,logger
logger = logger
API_ENDPOINT = getenv("API_ENDPOINT", "http://localhost:5000")