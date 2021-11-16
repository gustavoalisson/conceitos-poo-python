
# * Principio de LISKOV = Mesma funcionalidade para os mesmos objetos

class Pessoa:
    def se_apresentar(self):
        print('Olá!! O meu nome é Alisson.')
        
class PessoaB(Pessoa):
    def __init__(self) -> None:
        super().__init__()
    
    def se_apresentar(self):
        print('Estou alterando esse metodo haha!')    

pessoa = Pessoa()

pessoa.se_apresentar()

# def apresentar_novamente():
#     print('Olá.... Estou mudando a minha apresentação!')        
    
# pessoa.se_apresentar = apresentar_novamente

# pessoa.se_apresentar()    