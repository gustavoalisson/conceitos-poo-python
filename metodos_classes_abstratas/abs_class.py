from abc import ABC, abstractmethod

class AbastractClass(ABC):
    def __init__(self) -> None:
        self.atributo = 'Olá mundo'
    
    def metodo(self, elemento: str) -> None:
        print(elemento)
    
    @abstractmethod
    def metodo_abstrato(self) -> None:
        pass
        
        