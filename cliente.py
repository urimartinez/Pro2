class Cliente(Persona):
    def __init__(self,nombre,dni,contacto):
        super().__init__(nombre,dni,contacto)
        self.tipo_usuario="Cliente"
    def mostrar_cliente(self):
        return f"{self.mostrar_datos()}, tipo de usuario: {self.tipo_usuario}"
