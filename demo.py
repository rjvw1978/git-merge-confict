from modulos.suma import Suma
from modulos.resta import Resta

num1=2
num2=3

operacionSuma=Suma(num1,num2)
operacionSuma.sumar()
print(operacionSuma.resultado)

operacionResta=Resta(78,788)
operacionResta.restar()
print(operacionResta.resultado)
