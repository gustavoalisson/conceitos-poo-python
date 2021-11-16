from abc import ABC, abstractmethod

# Essa interface força a implementar os metodos abaixo

class FormasInterface(ABC):
    
    @abstractmethod
    def get_perimetro(self) -> int:
        pass
    
    @abstractmethod
    def get_area(self) -> int:
        pass