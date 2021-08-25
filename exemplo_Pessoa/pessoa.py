from datetime import datetime
from random import randint

class Pessoa:
    # atributo da classe
    ano_atual = int(datetime.strftime(datetime.now(), '%Y')) 
    
    # atributos da instancia
    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    
    # * Métodos de instância
    def falar(self, dialogo):
        if self.comendo:
            print(f'{self.nome} não pode falar de boca cheia.')
            return 
            
        print(f'{self.nome} disse: {dialogo}')
        self.falando = True 
                
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        print(f'{self.nome} parou de falar.')
        self.falando = False
                
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return

        if self.falando:
            self.comendo = False
            print('Você está falando, não pode comer ao mesmo tempo.')
            return         
        
        self.alimento = alimento
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True    

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo...')
            return
        
        print(f'{self.nome} parou de comer!')
        self.comendo = False
    
    def get_ano_nascimento(self):
        nascimento =  self.ano_atual - self.idade
        print(f'O ano de nascimento de {self.nome} foi em {nascimento}')

# * Utilizo esse metodo para ser relacionado a classe, o molde geral.  
# * Não necessita de instância para usa-lo  
    @classmethod    
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

# * Não necessita da instância e nem da classe
# ! não pode utilizar self ou cls    
    @staticmethod
    def gera_id_pessoa():
        rand = randint(10000, 19999)
        return rand    