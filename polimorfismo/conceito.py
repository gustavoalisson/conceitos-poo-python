class PessoaA:
    
    def se_apresentar(self):
        print('Olá, eu sou a pessoa A.')

class PessoaB(PessoaA):
    
    def __init__(self) -> None:
        super().__init__()
    
    def se_apresentar(self):
        print('Alterando o metodo')

class PessoaC(PessoaB):
    def __init__(self) -> None:
        super().__init__()

pessoa = PessoaA()
pessoa2 = PessoaB()
pessoa3 = PessoaC()

pessoa.se_apresentar()
pessoa2.se_apresentar()        
pessoa3.se_apresentar()        