# Apenas introdução
# Class: Abstração de algum elemento natural que possui ações (metodos) e caracteristicas (atributos). 
# self: passa como parâmetro dentro de uma classe para indicar que está em um contexto de uma classe
class Minha_Classe:
    
    # metodo construtor
    def __init__(self, recebe_algo):
        self.meu_atributo = 'Olá mundo'
        self.meu_atributo2 = recebe_algo
    
    def meu_metodo(self):
        print(self.meu_atributo)
        print(self.meu_atributo2)
    
    def meu_metodo2(self, num, mult):
        return num * mult        

objeto = Minha_Classe('Alisson Gustavo')
objeto.meu_metodo()