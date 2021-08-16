class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__
    
    def falar(self):
        print(f'A classe {self.nomeClasse} que está falando...')
        print(f'{self.nome} falando...')    
    

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeClasse} está comprando')
  

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeClasse} está estudando')    
        
            