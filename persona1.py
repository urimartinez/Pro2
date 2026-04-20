class Persona:
    #atributos
    def __init__(self, nombre,dni,contacto):
        self._nombre = nombre #encapsulamiento - protegido
        self.__dni = dni #encapsulamiento - privado
        self._contacto=contacto #encapsulamiento - protegido
    #metodos funciones de las clases
    @property
    def dni(self):
        return self.__dni
    def mostrar_datos(self):
        return f"Nombre:{self.nombre}, DNI:{self.dni}, Tel:{self.contacto}"
    def identificarse (self):
        return f"Soy {self.nombre} con DNI {self.dni}"
    