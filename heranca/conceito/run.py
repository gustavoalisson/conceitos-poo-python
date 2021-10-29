class Mae:
    
    def __init__(self, nome) -> None:
        self.endereco = 'Rua do Balão Mágico'
        self.nome = nome
        self.sobrenome = 'Santos'
        
    def comer(self) -> None:
        print('Estou comendo! nhac nhac nhac')
        
    def estudar(self) -> None:
        print('Estou estudando... *--*')
        
    def apresentar_nome(self) -> None:
        print(f'{self.nome} {self.sobrenome}')        

class Pai:
    
    def __init__(self, alguma_coisa) -> None:
        self.alguma_coisa = alguma_coisa      

class Filha(Mae):
    
    def __init__(self, nome) -> None:
        super().__init__(nome) # Super = Se referir a classe Mae e o init se refere ao construtor da classe Mae
    
    def brincar(self, brinquedo: str) -> None:
        print(f'Estou brincando com {brinquedo}')
        
mae = Mae('Jamilly')
filha = Filha('Maria')
# filha.estudar()
# print(filha.alguma_coisa)
print(filha.nome)
filha.apresentar_nome()
mae.apresentar_nome()
filha.brincar('boneca')