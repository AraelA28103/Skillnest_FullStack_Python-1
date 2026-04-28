"""Realizar las siguientes pruebas con instancias:

Crea 3 usuarios de la plataforma de streaming.
Haz que el primer usuario agregue dos títulos a su lista y los vea.
Haz que el segundo usuario agregue un título, lo vea y cambie su suscripción.
Haz que el tercer usuario agregue tres títulos, los vea y cambie su suscripción dos veces."""

class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = []

    def agregar_a_lista(self, titulo):
        """Agrega un contenido a la lista de reproducción del usuario."""
        self.lista_reproduccion.append(titulo)
      

    def ver_contenido(self, titulo):
        """Simula que el usuario reproduce un contenido."""
        pass

    def cambiar_suscripcion(self, nueva_suscripcion):
        """Cambia el tipo de suscripción del usuario."""
        pass

    def mostrar_info_usuario(self):
        """Muestra la información del usuario y su lista de reproducción."""
        pass
    
# Todos los valores que se deban registrar deben ser con input 
#Añadir unmenu while para llamar a los metodos
# (Menu de seleccion) 

titulo = input("Ingresa alguna cuestiion: ")
