class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome # * publico
        self.idade = idade
        self.__cpf = cpf # * privado

    def correr(self):
        print('Estou correndo...')
    
    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
        print('bebendo...')    
    
    def __apresentar_documento(self)        :
        print(self.__cpf)

pessoa = Pessoa('Alisson', 24, 111557710098)
# objeto não tem acesso ao atributo __cpf que está privado, apenas a classe consegue acessar
# print(pessoa.cpf)        
pessoa.beber('cerveja')