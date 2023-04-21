import time
import os
import constants
from file_types import getContentType


def post(path):

    #Se busca el archivo en ruta especificada por la petición
    path = path[1:]
    rt = os.getcwd()
    new_path = os.path.join(str(os.path.dirname(rt)), path)


    file = open(new_path, 'r')
    file = file.read()
    file_stat = os.stat(new_path)

    #Se determinan las diferentes cualidades del archivo y se establece la fecha de la petición
    ttime = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
    content_type = getContentType(new_path)
    content_length = file_stat.st_size
    last_modified = file_stat.st_mtime

    etag_str = str(last_modified) + str(content_length)
    etag_str = hash(etag_str)

    etag = hex(etag_str)[2:]
    last_modified = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(last_modified))

    #Respuesta a la petición
    answer = {
        'Date' : ttime,
        'Content-Type' : f'{content_type} ; {constants.ENCONDING_FORMAT}',
        'Content-Length' : content_length,
        'file' : file,
        'ETag' : etag,
        'Last-Modified' : last_modified
    }

    return answer