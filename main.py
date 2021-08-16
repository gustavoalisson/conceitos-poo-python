class BaseDeDados:
    def __init__(self):
        self.__dados = {} 
    
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})        

    def lista_clientes(self):
        print('-------------- LISTA DE CLIENTES --------------')
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
    
    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]
         
    
base = BaseDeDados() 
# base.inserir_cliente(1, 'Alisson')
# base.inserir_cliente(2, 'Gustavo')
# base.inserir_cliente(3, 'Santos')  
# base.apaga_cliente(1)
# base.lista_clientes()
base.__dados = 'a'
print(base.__dados)
print(base._BaseDeDados__dados)