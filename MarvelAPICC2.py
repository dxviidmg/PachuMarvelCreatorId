import requests
import hashlib


class PachuMarvel(object):
    """Ingresa llaves publica y privada, en caso de no ingresar, utiliza las default"""
    def __init__(self, public_key='612692101a6afb6eaacb7e4d81007613', private_key='a8a98daeb478e11f73a003224697722ef63abe39'):
        self.public_key = public_key
        self.private_key = private_key
        ts = '1'
        self.ha = hashlib.md5((ts+self.private_key+self.public_key).encode()).hexdigest()
        self.url = 'http://gateway.marvel.com/v1/public/'
        
        self.creador = None
        self.idc = ''
        self.fullName = ''
        self.img=''
        self.formato=''
        self.imagen=''
        self.eventos=''

    def get_creador(self, idc=1):
        """Escribe el nombre de un personaje"""
        try:
            self.creador = requests.get(
                self.url+'creators/'+str(idc),
                params={
                    'apikey': self.public_key,
                    'ts': '1',
                    'hash': self.ha,
                    }).json()
        except Exception as e:
            print("Error,",e)
    def get_response(self):
        try:
            print(self.creador)
        except:
            print("Primero llama a get_creator")
    def get_dataimp(self):
        try:
            self.fullName = self.creador['data']['results'][0]['fullName']
            self.img = self.creador['data']['results'][0]['thumbnail']['path']
            self.formato = self.creador['data']['results'][0]['thumbnail']['extension']
            self.eventos = self.creador['data']['results'][0]['events']['items']
            self.imagen = self.img +"."+self.formato

            print("Nombre Completo: ", self.fullName)
            print("Imagen: ", self.imagen)
            print("Eventos: ", self.eventos)
            
        except Exception as e:
            print("Error,",e)
