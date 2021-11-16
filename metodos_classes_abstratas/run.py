from abs_class import AbastractClass

class Filha(AbastractClass):
    
    def apresentar_metodo(self) -> None:
        print(self.atributo)
    
    def metodo_abstrato(self) -> None:
        print('Implementando meu metodo abstrato')
    

filha = Filha()
filha.apresentar_metodo()
filha.metodo('Cheguei aqui!!')
filha.metodo_abstrato()

# abstract = AbastractClass()
# abstract.metodo('Fazendo algo por aqui')