import time
import os
import constants
from file_types import getContentType


def error(file_path:str):

    #Se busca el archivo en ruta especificada por la petición
    file_path = file_path[1:]
    current_directory = os.getcwd()
    new_file_path = os.path.join(str(os.path.dirname(current_directory)), file_path)

    #Se lee el archivo
    file = open(new_file_path, 'r')
    file = file.read()

    #Se determinan las diferentes cualidades del archivo y se establece la fecha de la petición
    ttime = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
    content_type = getContentType(new_file_path)
    content_length = os.path.getsize(new_file_path)

    #Respuesta a la petición
    answer = {
        'Date' : ttime,
        'Content-Type' : f'{content_type} ; {constants.ENCONDING_FORMAT}',
        'Content-Length' : content_length,
        'file' : file
    }

    return answer