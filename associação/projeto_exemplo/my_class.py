class Interruptor:
    def __init__(self, comodo) -> None:
        self.__comodo = comodo
    
    def acender(self):
        print(f'Acendendo {self.__comodo}')
    
    def apagando(self):
        print(f'Apagando {self.__comodo}')        