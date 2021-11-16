from typing import Type
from interfaces.formas import FormasInterface
from terrenos.retangular import TerrenoRetangular

class Engenheiro:
    
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def medir_terreno(self, terreno: Type[FormasInterface]):
        perimetro = terreno.get_perimetro()
        print(f'{self.nome} mediu o perimetro {perimetro}')

    def medir_area(self, terreno: Type[FormasInterface]):
        area = terreno.get_area()
        print(f'{self.nome} mediu a area {area}')

terreno = TerrenoRetangular(10 , 10)
engenheiro = Engenheiro('Alisson')

engenheiro.medir_terreno(terreno)        