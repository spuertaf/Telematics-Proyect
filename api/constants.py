#PORT: int, puerto en el que se escucharan las peticiones
#ENCONDING_FORMAT: string, formato en el que se codificaran las peticiones
#RECV_BUFFER_SIZE: int, trama;o maximo del buffer
#IP_SERVER: string, IPv4 privada del servidor
#GET: string, tipo de petición
#HEAD: string, tipo de petición
#POST: string, tipo de petición
#QUIT: string, tipo de petición
#SERVER: string, servidor que enviara constesta las peticiones
#E404: string, archivo que muestra el error 404
#E405: string, archivo que muestra el error 405
#E400: string, archivo que muestra el error 400

PORT = 8080
ENCONDING_FORMAT = "UTF-8"
RECV_BUFFER_SIZE = 4096
IP_SERVER = '127.0.0.1'
KEEP_ALIVE_TIMEOUT = 5
GET = 'GET'
HEAD = 'HEAD'
POST = 'POST'
QUIT = 'QUIT'
SERVER = 'Apache/2.4.41 (Ubuntu)'
E404 =  '/api/error/html_errors/error404.html'
E405 =  '/api/error/html_errors/error405.html'
E400 =  '/api/error/html_errors/error400.html'