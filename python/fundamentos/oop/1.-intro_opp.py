#Creacion de la clase usuario - entidad

class Usuario:
   def __init__(self): #constructor
       self.nombre = "Nariyoshi"
       self.apellido = "Miyagi"
       self.email = "miyagi@codingdojo.la"
       self.limite_credito = 30000
       self.saldo_pagar = 0

#Instancias de una clase

miyagi = Usuario()
daniel = Usuario()
yuli = Usuario()

#Accedemos a los atributos de la instancia
print(miyagi.apellido) #Imprime: Nariyoshi
print(miyagi.nombre) #Imprime: Miyagi
print(miyagi.email) #Imprime: miyagi@codingdojo.la
print(miyagi.limite_credito) #Imprime: 30000
print(miyagi.saldo_pagar) #Imprime: 0


# Nuevos valores asignados a atributos de la instancia

daniel.nombre = "Daniel"
daniel.apellido = " Larusso"
daniel.email = "daniel@gmail.com"
daniel.limite_credito = 30000
daniel.saldo_pagar = 20000

print(daniel.nombre) #Imprime: Daniel

#Valores a nuevas instancias
yuli.nombre = "Yulieth"
yuli.apellido = "Gonzalez"
yuli.email = "yulieth@gmail.com"
yuli.limite_credito = 20000
yuli.saldo_pagar = 0

#Imprimir nombre de cada instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel
print(yuli.nombre) #Imprime: Yulieth


