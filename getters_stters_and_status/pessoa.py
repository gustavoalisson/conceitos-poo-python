
# ! Importe criar nomes de classe / atributos com substantivos e nomes de metodos com verbos
class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
    
    def dirigir(self, veiculo: str) -> None:
        print(f'Dirigindo um(a) {veiculo}')
    
    def cantar(self) -> None: 
        print('cantando... lalala')
    
    def apresentar_idade(self) -> int:
            return self.idade