class MinhaClasse:    
    # contexto de classe, "geral"
    estatico = 'Cachorro'
    
    def __init__(self, estado) -> None:
        self.estado = estado
    
    def print_estatico(self):
        print(self.estatico)
        # Nessa abordagem o self é a mesma cosia que o "obj1" por exemplo, pq está utilizando o contexto passado ao objeto  
    @classmethod
    def mudar_estatico(cls, valor):
        cls.estatico = valor
    
obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)

obj1.mudar_estatico('Gato')

obj1.print_estatico()
obj2.print_estatico()
