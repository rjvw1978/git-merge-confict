from modulos.operacion import Operacion

class Suma(Operacion):
    def __init__(self, valorA, valorB):
        super().__init__(valorA, valorB)
    
    def sumar(self):
        self.resultado= self.valorA + self.valorB