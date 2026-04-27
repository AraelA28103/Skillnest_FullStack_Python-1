# Pasar argumentos 
"""Para poder personalizar nuestras instancia vamos a pasar 
algunos argumentos al método __init__ y que de esta manera 
podamos asignarle a los atributos los valores correspondientes.g"""

class Usuario:
   def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = limite_credito
       self.saldo_pagar = saldo_pagar

#Creacion de las instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 30000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 40000, 20000)
yuli = Usuario("Yulieth", "Gonzalez", "yulieth@gmail.com", 50000, 30000)

#Imprimimos valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel
print(yuli.nombre) #Imprime: Yulieth


#Tarea
"""
Crea una clase Estudiante, y asignarle los siguientes atributos:
(rut, nombre, apellido, especialidad, fecha_nac)
-Crea 3 instancias para la clase con distintos estudiantes.
-Imprime el nombre y el apellido concatenado + especialidad
"""
class Estudiante:
    def __init__(self, rut, nombre, apellido, especialidad, fecha_nac):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.fecha_nac = fecha_nac
        
#Creacion de las instancias
isi = Estudiante("22796812-5", "Isidora", "Valenzuela", "Programación", "19-06-2008")
martin = Estudiante("22840632-5", "Martin", "Rojas", "Programación", "04-10-2008")
ara = Estudiante("23036981-k", "Arael", "Anabalon", "Programación", "06-06-2009")

print(f"{isi.nombre} {isi.apellido} ")