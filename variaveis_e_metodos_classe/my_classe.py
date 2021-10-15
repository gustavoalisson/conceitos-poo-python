# Um método de classe é um método vinculado à classe e não ao objeto da classe.
# Eles têm acesso ao estado da classe, pois leva um parâmetro de classe que aponta para a classe e não para a instância do objeto.
# Ele pode modificar um estado de classe que se aplicaria a todas as instâncias da classe. Por exemplo, ele pode modificar uma variável de classe que será aplicável a todas as instâncias.
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
