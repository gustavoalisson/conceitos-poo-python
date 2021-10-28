from typing import Type
class Casa:
    def __init__(self, dono_casa) -> None:
        self.__dono_casa = dono_casa
        self.__endereco = '1° Rua do Rosário'
    
    def acender_luzes(self) -> None:
        print('Estou acendendo as luzes!!')
    
    def get_endereco(self) -> str:
        return self.__endereco
    
    def proprietario(self) -> str:
        return self.__dono_casa
    
class Pessoa:
    def __init__(self, nome: str, local: Type[Casa]) -> None:
        self.__local = local
        self.__nome = nome
    
    def entrar_no_local(self) -> None:
        self.__local.acender_luzes()
    
    def apresentar_local(self) -> None:
        endereco = self.__local.get_endereco()
        print(endereco)
    
    def apresentar_proprietario(self) -> None:
        prop = self.__local.proprietario()
        print(f'Dono da casa: {prop}')    

casa_amigo = Casa('Luiz')
pessoa = Pessoa('Alisson', casa_amigo)        

pessoa.entrar_no_local()
pessoa.apresentar_proprietario()
pessoa.apresentar_local()