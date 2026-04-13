class Vehiculo:
    def __init__(self, modelo, color, tipo_vehiculo, patente):
        self.modelo=modelo
        self.color=color
        self.tipo_vehiculo=tipo_vehiculo
        self.patente=patente
    def mostrar(self):
        print(self.modelo, self.color,self.tipo_vehiculo,self.patente)
        