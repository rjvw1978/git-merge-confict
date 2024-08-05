from modulos.operacion import Operacion

class Resta(Operacion):
    def __init__(self, valorA, valorB):
        super().__init__(valorA, valorB)
    
    def restar(self):
        self.resultado= self.valorA - self.valorB