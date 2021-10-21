from typing import Type
class Interruptor:
    def __init__(self, comodo) -> None:
        self.__comodo = comodo
    
    def acender(self):
        print(f'Acendendo {self.__comodo}')
    
    def apagar(self):
        print(f'Apagando {self.__comodo}')        
        
class Pessoa:
    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender()
    
    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar()
    
    def dormir(self):
        print('Partiu!!! Dormir...')

pessoa = Pessoa()
quarto = Interruptor('quarto') 
cozinha = Interruptor('cozinha')

quarto.acender()
pessoa.acender_luz(cozinha)
pessoa.apagar_luz(quarto)
pessoa.dormir()