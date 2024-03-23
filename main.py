# Importar el módulo web2py
from gluon import *

# Definir la aplicación
mi_aplicacion =  request.application

# Definir el controlador para manejar las solicitudes
def index():
    return dict(message="¡Hola desde web2py!")

# URL de la ruta para el controlador index
routers = dict(
    BASE = dict(
        default_application=mi_aplicacion,
        default_controller='default',
        default_function='index',
    )
)
