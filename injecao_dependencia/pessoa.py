class Casa:
    def __init__(self, dono_casa) -> None:
        self.__dono_casa = dono_casa
        self.__endereco = '1° Rua do Rosário'
    
    def acender_luzes(self) -> None:
        print('Estou acendendo as luzes!!')
    
    def get_endereco(self) -> str:
        return self.__endereco
    
class Pessoa:
    def __init__(self, nome: str) -> None:
        self.__nome = nome
    
    def entrar_no_local(self, local: any) -> None:
        local.acender_luzes()
    
    def apresentar_local(self, local: any) -> None:
        endereco = local.get_endereco()
        print(endereco)

casa_amigo = Casa('Luis')
pessoa = Pessoa('Alisson')        

pessoa.entrar_no_local(casa_amigo)
pessoa.apresentar_local(casa_amigo)