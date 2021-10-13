import random

class ControleRemoto:
    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo
        self.power = False
    
    def ligar_tv(self):
        self.power = True
        self.canal_atual = random.randint(2, 22)
        print(f'Tv ligada! Canal atual {self.canal_atual}')
    
    def avancar_canal(self):
        print('Canal avançado!')
        self.recebe = self.canal_atual
        self.recebe += 1
        print(self.recebe)
    
    def voltar_canal(self):
        print('Voltar canal')
    
    def escolher_canal(self, canal):
        if canal != self.canal_atual:
            print(f'Alterado para o canal {canal}')
        else:
            print(f'Assistindo o canal atual: {self.canal_atual}')    
            

controle_sala = ControleRemoto('Samsung', 'sala')

controle_sala.ligar_tv()
controle_sala.escolher_canal(2)
controle_sala.avancar_canal()